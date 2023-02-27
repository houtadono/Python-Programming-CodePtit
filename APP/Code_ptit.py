import os
import pathlib
import shutil
import time
from bs4 import BeautifulSoup
from selenium.webdriver import EdgeOptions, Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from threading import Thread, Barrier
import config

class Exercise:
    def __init__(self, id, name, group, topic, level, check_class) :
        self.id = id
        self.name = name
        self.group = group
        self.topic = topic
        self.level = level
        if check_class == 'bg--10th': self.color = "Green"
        elif check_class == 'bg--50th': self.color = "Red"
        else: self.color = "White"
        pass    

    def __lt__(self, obj):
        if self.level == obj.level:
            return self.id < obj.id
        return self.level < obj.level

    def info(self):
        return f"Tiêu đề: {self.name}\nNhóm: {self.group}\nChủ đề: {self.topic}\nĐộ khó: {self.level}"

class CodePtit:

    ID = []
    EXERCISES = {}
    TOPIC = []

    def __init__(self):
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # edge_options.add_argument("--headless")
        # edge_options.add_argument("user-data-dir=C:\\Users\\Houta\\AppData\\Local\\Microsoft\\Edge\\User Data1")
        self.driver = Edge( service=Service('./script/msedgedriver.exe'), options= edge_options)
        self.driver.set_window_size(800,800) 
        self.time = time.time()
        pass

    def login(self, username, password):
        self.driver.get('https://code.ptit.edu.vn/login')
        self.driver.implicitly_wait(3)   
        self.driver.find_element(By.ID, 'login__user').send_keys(username)
        self.driver.find_element(By.ID, 'login__pw').send_keys(password)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[3]/div/form/button').click()
        self.username = username
        self.password = password 
        if self.driver.current_url != 'https://code.ptit.edu.vn/login':
            print('Dang nhap thanh cong')
            return True, "ok"
        else:
            invalid = self.driver.find_element(By.CLASS_NAME, 'login__main__invalid').text
            print(invalid)
            return False, invalid     
        
    def load_exercise_no_thread(self):
        while True:
            # load page
            list_tr = self.driver.find_elements(By.TAG_NAME, 'tr')  
            for i in range(1, len(list_tr)): 
                list_td = list_tr[i].find_elements(By.TAG_NAME, 'td')  
                name_ex  = list_td[3].text
                group_ex = list_td[4].text
                topic_ex = list_td[5].text
                id_ex    = list_td[2].text

                if topic_ex not in self.TOPIC:
                    self.TOPIC.append(topic_ex)

                self.EXERCISES[id_ex] = Exercise(id_ex, name_ex, group_ex, topic_ex, list_tr[i].get_attribute('class') == 'bg--10th')
            try:
                self.driver.find_element(By.LINK_TEXT, '»' ).click()
            except:
                break

    def create_thread(self):
        self.page_count = len(self.driver.find_elements(By.CLASS_NAME, 'page-item')) - 2
        self.barrier = Barrier(self.page_count)

        self.list_browser = [self]
        for i in range(self.page_count-1):
            a = CodePtit()
            a.login(self.username,self.password)
            self.list_browser.append(a)

        self.list_thread = []
        for i in range(self.page_count):
            t = Thread(target=CodePtit.load_exercise_each_thread, 
                args=(self.list_browser[i],self.barrier,i+1, self.TOPIC, self.EXERCISES) )                
            t.start()
            self.list_thread.append(t)

        for e_thread in self.list_thread:
            e_thread.join()
        
        tmp = sorted(self.EXERCISES.items(), key=lambda k: k[1])
        self.ID = list(map(lambda x : x[0], tmp))
        self.TOPIC = sorted(self.TOPIC)

    def load_exercise_each_thread(browser, barrier, page_idex, topic, exercise):
        browser.driver.get('https://code.ptit.edu.vn/student/question?page=%d' %(page_idex))
        browser.driver.implicitly_wait(1)   
        barrier.wait()

        list_tr = browser.driver.find_elements(By.TAG_NAME, 'tr')  
        for i in range(1, len(list_tr)): 
            list_td = list_tr[i].find_elements(By.TAG_NAME, 'td')  
            id_ex    = list_td[2].text
            name_ex  = list_td[3].text
            group_ex = list_td[4].text
            topic_ex = list_td[5].text
            level_ex = list_td[6].text

            if topic_ex not in topic:
                topic.append(topic_ex)
            exercise[id_ex] = Exercise(id_ex, name_ex, group_ex, topic_ex, level_ex, list_tr[i].get_attribute('class'))

        if page_idex != 1:
            browser.driver.quit()

    def find_exs_by_id_or_name(self, key_search):
        key_search = config.khongdau(key_search)
        return [id for id in self.ID if key_search in config.khongdau(id.lower()) or key_search in config.khongdau(self.EXERCISES[id].name.lower())]

    def auto_create_file_exercise(self, folder = False):
        if folder:
            for id in self.ID:
                old_path = './%s.py' %(id)
                target_path = './%s/%s.py' %(self.EXERCISES[id].topic, id)
                if os.path.exists(old_path):
                    shutil.copyfile(old_path, target_path)
                elif os.path.exists(target_path):
                    pass
                else:
                    pathlib.Path('./%s' %(self.EXERCISES[id].topic)).mkdir(exist_ok= True)
                    pathlib.Path(target_path).touch(exist_ok= True)
                if os.path.getsize(filename=target_path) == 0:
                    with open(target_path,'w') as file:
                        file.write("# empty")

        else:
            for id in self.ID:
                old_path = './%s.py' %(id)
                pathlib.Path('./%s.py' %(id)).touch(exist_ok= True)

        print("done")

    def see_ex(self, id):
        self.driver.get('https://code.ptit.edu.vn/student/question/%s' %(id))
        k =self.driver.find_element(By.CLASS_NAME, 'submit__des')
        html = k.get_attribute('outerHTML')
        attrs = BeautifulSoup(html, 'html.parser')
        return attrs

    def upload_code(self,id):
        self.driver.get('https://code.ptit.edu.vn/student/question/'+id)
        self.driver.find_element(By.ID, 'fileInput').send_keys(os.path.abspath( id+'.py' ))
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[4]/form/button').click()
    


# a = CodePtit()
# a.login('b20dcat066','t1 houta1')
# a.create_thread()
# a.auto_create_file_exercise(True)

# attrs = a.see_ex('ICPC0115')

# b = attrs.p
# while b != None:
#     if b.name == None:
#         b = b.next_sibling
#         continue
#     print(b.name)
#     b.find('span')
#     for x in b:
#         if hasattr(x,'text'):
#             if not x.text.isspace():
#                 print(f"111{x.text}111")
#     b = b.next_sibling

# a.create_thread()
# a.load_exercise_no_thread()


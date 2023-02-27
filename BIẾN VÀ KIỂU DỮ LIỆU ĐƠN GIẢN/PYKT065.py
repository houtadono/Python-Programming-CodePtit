
import itertools as itt 
while True: 
    _ = input() 
    if _ == "-1": break  
    # Input 
    L, R = [int(x) for x in _.split()] 
    N = int(input()) 
    # Init Base Prime 
    BasePrime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] 
    while BasePrime[-1] > N: 
        BasePrime.pop(-1) 
        CountBasePrime = len(BasePrime) 
        # Init Count All 
        CountAll = R - L + 1 
        # Lets Go 
        CountDivisible = 0 
        for CountPrime in range(1, CountBasePrime + 1): 
            ListCombination = itt.combinations(BasePrime, CountPrime) 
            for combination in ListCombination: 
                MultiplyAllElement = 1 
                for element in combination: 
                    MultiplyAllElement *= element 
                    _min = int( L / MultiplyAllElement) if L % MultiplyAllElement == 0 else int( L / MultiplyAllElement) + 1 
                    _max = int(R / MultiplyAllElement) 
                    _count = _max - _min + 1 
                    if CountPrime % 2 == 1: CountDivisible += _count 
                    else: CountDivisible -= _count 
            print(CountAll - CountDivisible)
# empty

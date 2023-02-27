
import math

for _ in range(int(input())):
    print( math.prod( 
        map( int, input().replace('0','') ) 
        ) )

# done
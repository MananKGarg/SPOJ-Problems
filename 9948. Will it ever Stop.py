""" A little observation tells us that only powers of two would be able to stop and rest would continue indefinitely.
 Bitwise operation on any power of 2 and 1 less than the number gves 0.
 8 = 1000
 7 = 0111
 
 8 & 7 = 0000
 
"""

def IsPowerOfTwo(x):
    return(x and (not( x & (x-1))))

n = int(input())
if(IsPowerOfTwo(n)):
    print('TAK')
else:
    print('NIE')

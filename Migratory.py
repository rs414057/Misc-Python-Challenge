

import sys
print '''
A flock of birds is flying across the continent. Each bird has a type, and the different types are designated by the ID numbers , , , , and .
Given an array of integers where each integer describes the type of a bird in the flock, find and print the type number of the most common bird. If two or more types of birds are equally common, 
choose the type with the smallest ID number.
      '''

def migratoryBirds(n, ar):
    # Complete this function
    n=max(ar,key=ar.count)
    return n
                
            

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)

import sys

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot=array[0]
        lower=[i for i in array [1:] if i <= pivot]
        higher=[i for i in array [1:] if i >= pivot]

        return quickSort (lower) + [pivot] + quickSort (higher)

print (quickSort([1,4,8,11,7,6,10,5,2,9,3]))

import sys
def countDown(i):
    print (i)
    if i <= 0:
        return
    else:
        countDown(i-1)

print(countDown(5))
#Selection sort by min to max
import sys

#elements to be sorted
A = [64,25,12,22,11,3,94,80,44,56,63,62,61]
#put them in a for each for all elements
for i in range(len(A)):

    #find the min element in the unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    
    #exchange the found min elements with the first one
    A[i], A[min_idx] = A[min_idx], A[i]

#Test the code
print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i]),
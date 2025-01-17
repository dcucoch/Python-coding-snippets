import sys
def countDown(i):
    print (i)
    if i <= 0:
        return
    else:
        countDown(i-1)

print(countDown(5))
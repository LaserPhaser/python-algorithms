# Uses python3
import sys
import random
''' # quadratic time check
def quadratic_time (a):
    for i in range(len(a)):
        count = 0 
        for j in range(i,len(a)):
            if a[j] == a[i]:
                count += 1
        if count > len(a)//2:
            return a[i]
'''
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid = left + (right - left ) //2
    ret1 = get_majority_element(a[left:mid], 0, mid)
    ret2 = get_majority_element(a[mid:right + 1], 0, mid)
    if ret1 == ret2:
        return ret1
    check1 = 0
    check2 = 0
    for i in range(len(a)):
        if a[i] == ret1:
            check1 += 1
        if a[i] == ret2:
            check2 += 1
    if (check1 > mid  ):
        return ret1
    if (check2 > mid ):
        return ret2
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #n, *a = list(map(int, "9 2 1 1 2 2 1 2 1 1".split()))
    #print (a)
    #n, *a = list(map(int, "4 1 2 3 4".split()))
    #n, *a = list(map(int, "5 12 12 12 12 12".split()))

    ### start to remove
    ''' s=""
    for x in range(random.randint(1, 10)):
        s += " " + str(random.randint(1, 10) )
    a = str(s).split()
    
    n=x+1
    print (a, n)
    ### end to remove
    '''
    #print ("mj",get_majority_element(a, 0, n))
    #print (quadratic_time(a))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    i = l
    k = r
    while i <= k:
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            j += 1
        elif a[i] > x:            
            a[i], a[k] = a[k], a[i]
            k -= 1
        else:
            i += 1
    return j , k



def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)

    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)
    return a


def binary_search(a, x):
    left, right = 0, len(a)
    left = 0 
    right = (len(a)-1)
    # write your code here
    while left <= right:
        mid = left + (right - left) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left 



def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    if(len(ends)>1):
        ends = randomized_quick_sort(ends,0 , len(ends)-1)

    if(len(starts)>1):
        starts = randomized_quick_sort(starts,0 , len(starts)-1)
    
    indexes = sorted(range(len(points)),key=lambda x:points[x])
    if (len(points) >1 ):
        points = randomized_quick_sort(points,0 ,len(points)-1)
    ll = randomized_quick_sort(starts + ends + points,0 , len(starts + ends+ points)-1)

    point = 0
    s ,e ,p = 0, 0, 0
    ind = 0
    i = 0
    mp, ms ,me = 1, 1, 1
    while i < len(ll)-1:
        if (len(starts)> s and ll[i] == starts[s]):
            ms = 0
            while len(starts)> s and ll[i] == starts[s]:
                ms += 1
                s += 1
                #print ("ms",ms)
                point += 1
        if (len(points) > p and ll[i] == points[p]):
            mp = 0
            while len(points) > p and ll[i] == points[p]:
                mp += 1
                cnt[indexes[p]] = point
                #print ("mp",mp)
                p += 1    
        if (len(ends) > e and ll[i] == ends[e]):
            me = 0
            while len(ends) > e and ll[i] == ends[e]:
                me += 1
                e +=1
                #print ("me",me)
                point -= 1
        #print (ms,mp,me)
        #print (i)
        i += min(ms,mp,me)

            

    #ll = starts+ends+points
    #print(ll)
    #for j in range(len(starts+ends+points)):
        #if ll[i]
     #   cnt[i] += 1

    '''
            ind = 0
            ind2 = 0
            ind = binary_search(starts, points[i])
            if (ind == 0):
                cnt[i] = 0
                continue
            subends = ends[:ind]
            ind2 = binary_search(subends, points[i])
            if (ind2 == len(subends)):
                cnt[i] = 0
                continue;
            ind += 1
            ind2 = len(subends)-ind2

            cnt[i] = min(ind, ind2)
        '''
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = list(map(int, "3 2 -5 0 -3 2 7 10 -1 6".split()))
    #data = list(map(int, "3 3 5 5 5 5 5 5 5 5 5".split()))
    #data = list(map(int, "1 3 -10 10 -100 100 0".split()))
    #data = list(map(int, "2 3 0 5 7 10 1 6 11".split()))
    #data = list(map(int, "3 4 0 5 -3 2 7 10 0 -3 1 6".split()))
    '''
    #for i in range(1000):
    data1=""
    for x in range( 5):
        a1 = str(random.randint(5, 5))
        data1 += " "+ a1 + " " + str(random.randint(int(a1), 7) )
    print (data1)
    for x2 in range( 5):
        data1 += " " + str(random.randint(5,5) )
    data1=(list(mapa(int, str(data1).split())))
    data1.insert(0, x2+1)
    data1.insert(0, x+1)
    data = data1
    print ("start")
    print(data)
    '''
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    '''
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt2 = naive_count_segments(starts, ends, points)
    #print(data)

    if (cnt != cnt2):
        print (data, cnt, cnt2)
    else:
        print ("+1")
    '''
    for x in cnt:
        print(x, end=' ')

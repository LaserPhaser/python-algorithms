# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    
    min_num_ops = []
    min_num_ops.append(0)
    for i in range(1,n +1 ):
        a=n
        b=n
        if i % 3 == 0:
            a = min_num_ops[i // 3] + 1
        if i % 2 == 0:
            b = min_num_ops[i // 2] + 1
        c = min_num_ops[i - 1] + 1
        #print ("c", c)
        min_num_ops.append(min(a, b ,c))
       # print(i, min_num_ops ,a ,b ,c)
    #   print (min_num_ops)
    #print (min_num_ops[0:11])
    i = min_num_ops[-1]
    sequence.append(n)
    while  i > 1 :
        if (n % 3 ==0 and min_num_ops[n//3]  == i - 1 ):
            sequence.append(n//3)
            n = n//3
        elif( n%2 ==0 and min_num_ops[n//2] == i - 1 ):
            sequence.append(n//2)
            n = n//2
        else:
            sequence.append(n-1)
            n = n-1

        i -=1
    #sequence.append(n)
    return reversed(sequence)
    


input = sys.stdin.read()
n = int(input)
#n = 5
#n=96234
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

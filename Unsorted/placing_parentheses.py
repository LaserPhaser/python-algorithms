# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    operations = [x for x in dataset[1::2]]
    numbers = [x for x in dataset[::2]]
    minM = [[None for x in range(len(numbers))] for y in range(len(numbers))] 
    maxM = [[None for x in range(len(numbers))] for y in range(len(numbers))] 
    for i in range(len(numbers)):
        minM[i][i] = int(numbers[i])
        maxM[i][i] = int(numbers[i])    
    for s in range(1, len(numbers)):
        for i in range(0, len(numbers)-s):
            j = i + s 
            mini = 9999999999999999999999999999 
            maxi = -999999999999999999999999999
            for k  in range (i, j ):
                a = evalt(maxM[i][k], maxM[k+1][j], operations[k])
                b = evalt(maxM[i][k], minM[k+1][j], operations[k])
                c = evalt(minM[i][k], maxM[k+1][j], operations[k])
                d = evalt(minM[i][k], minM[k+1][j], operations[k])
                mini = min(mini, a, b, c, d)
                maxi = max(maxi, a, b, c, d)
            minM [i][j] = mini
            maxM [i][j] = maxi
    #print (maxM)
    #print ("\n\n\n\n",minM)
    return max(maxM[0][len(numbers)-1], minM[0][len(numbers)-1])


if __name__ == "__main__":
    print(get_maximum_value(input()))
    #print(get_maximum_value("9*9*9*9*9*9*9*9*9*9*9*9*9*9*9*9*9"))
    #print(get_maximum_value("1+5"))
    #print(get_maximum_value("3*5+8"))
    #print(get_maximum_value("32"))

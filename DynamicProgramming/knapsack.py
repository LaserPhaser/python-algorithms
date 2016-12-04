# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0   
    array = [[0 for x in range(W+1)] for y in range(len(w)+1)] 
    for i in range(1, len(w) + 1):	
	    for x in range(1, W + 1):
	    	array[i][x] = array[i-1][x]
	    	if (w[i-1] <= x ): 
	    		val =  w[i-1] + array[i-1][x-w[i-1]]
	    		if(array[i][x] < val):
	    			array[i][x] = val
    return array[i][x]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    #W, n, *w = list(map(int, "10 3 1 4 8".split()))
    #W, n, *w = list(map(int, "20 4 5 7 12 18".split()))
    print(optimal_weight(W, w))


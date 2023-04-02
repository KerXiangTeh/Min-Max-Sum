#!/bin/python3

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    #input validation
    if len(arr) != 5: 
        raise ValueError("Input is not of 5 elements!")
    if not all(isinstance(x, int) for x in arr): 
        raise ValueError("Not all elements are integers!")

    totalSum = sum(arr)
    minSum = totalSum - max(arr)
    maxSum = totalSum - min(arr)
    
    print(minSum, maxSum)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

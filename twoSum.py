# python program to check for the sum
# using binarysearch for (target - a[i]) on the remaining part
# step1. sort the arr
# step2. search for the difference of sum and element in arr

def binarySearch(arr, low, high, searchKey):
    middle = 0
    while(low<= high):
        middle = (high+low) // 2

        if(arr[middle]==searchKey):
            return 1
        
        if(arr[middle]<searchKey):
            low = middle+1
        else:
            high = middle -1

    # element not preset 
    return 0



def checkTwoSum(arr, arr_size, sum):
    # sort the arry 
    arr.sort()
    left = 0
    right = arr_size-1

    # traersing all elements in the array searching for searchKey
    i = 0

    while i< arr_size-1:
        searchKey = sum - arr[i]
        if(binarySearch(arr, i+1, right, searchKey)==1):
            return 1
        i+=1
    
    return 0

# Driver program to test the function 
if __name__ == '__main__':
    arr = [1, 4, 45, 6, 10, -8]
    n = 14

    if(checkTwoSum(arr, len(arr), n)):
        print("yes")
    else: 
        print("No")
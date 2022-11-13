

# Recursive binary search
def binary_search_r(arr, low, high, x):
    if(high>=low):
        middle = (high+low)//2

        # if element is present in the middle 
        if(arr[middle]==x):
            return middle
        
        elif(arr[middle]>x):
            return binary_search_r(arr, low, middle-1, x)
        
        else:
            return binary_search_r(arr, middle+1, high, x)
    else: 
        # element is not in the arry 
        return -1

# Iterative binary search
def binary_search_i(arr, x):
    low = 0
    high = len(arr) -1
    middle = 0

    while low<=high: 
        middle = (high+low) // 2

        if arr[middle] < x:
            low = middle +1 

        elif arr[middle]>x:
            low = middle -1
        
        else: 
            if(x == arr[middle]):
                return middle
            else: 
                return -1

    return -1




# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result_r = binary_search_r(arr, 0, len(arr)-1, x)
result_i = binary_search_i(arr, x)
 
print("Recursive approach: ")
if result_r != -1:
    print("Element is present at index", str(result_r))
else:
    print("Element is not present in array")

print("\nIterative approach: ")
if result_i != -1:
    print("Element is present at index", str(result_i))
else:
    print("Element is not present in array")
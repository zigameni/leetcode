
def findTriplets(arr, n):
    found = False
    for i in range(n-1):
        # find pairs with sum = -arr[i]
        s = set()
        for j in range(i+1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else: 
                s.add(arr[j])
            
    
    if  found == False:
        print("No Triplets FOund")

# Driver Code
arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)
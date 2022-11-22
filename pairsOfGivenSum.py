# Given an array of N integers, and a number sum,
#  the task is to find the number of pairs of integers
#  in the array whose sum is equal to sum.


def getPairsCount(arr, n, sum):
    s = set()
    count = 0
    for i in range(0, n):
        if arr[i] in s:
            count += 1
        else:
            s.add(sum - arr[i])

    return count


# Driver code
if __name__ == '__main__':
    arr = [1, 5, 7, -1]
    n = len(arr)
    sum = 6
    print("Count of pairs is",
          getPairsCount(arr, n, sum))

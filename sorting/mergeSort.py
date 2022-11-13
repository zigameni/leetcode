

def mergeSort(arr):
    if (len(arr) > 1):  # if the array is not empty

        # getting the middle of the array
        middle = len(arr)//2  # floor division

        # Dividing the array elements
        left = arr[:middle]
        right = arr[middle:]

        # Sorting by half
        mergeSort(left)

        mergeSort(right)

        # indexes
        i = j = k = 0

        # copy the data into temporaty arrays L[] and R[]
        while (i < len(left)) and (j < len(right)):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any elment was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def printArr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

    print()  # printing the new line


# Driver code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printArr(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printArr(arr)

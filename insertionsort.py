def insertionsort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

arr = [3, 6, 8, 10, 1, 2, 1]
insertionsort(arr)
print(arr)
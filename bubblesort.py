def bubblesort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = [3, 6, 8, 10, 1, 2, 1]
print(bubblesort(arr))
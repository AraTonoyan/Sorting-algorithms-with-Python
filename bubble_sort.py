def bubble_sort(arr):
    n = len(arr)
    swapped = True
    count = 0
    while swapped:
        swapped = False
        for i in range(n - count - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        count += 1


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:")
print(*arr)

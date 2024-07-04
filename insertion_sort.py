def insertion_sort(arr):
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1


arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array is:")
print(*arr)
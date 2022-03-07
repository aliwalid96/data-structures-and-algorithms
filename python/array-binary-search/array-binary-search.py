




def binarySearch(arr, n):
    start = 0
    end = len(arr) - 1
    mid = 0
    while start <= end:
        mid = (end + start) // 2
        if arr[mid] < n:
            start = mid + 1
        elif arr[mid] > n:
            end = mid - 1
        else: 
            return mid
    return -1
arr = [4, 7, 9, 16, 20, 25]
print(binarySearch(arr, 20))

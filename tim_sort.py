def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    
    i, j, k = 0, 0, l
    
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1

def tim_sort(arr):
    n = len(arr)
    min_run = calculate_min_run(n)
    
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)
    
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            
            if mid < right:
                merge(arr, left, mid, right)
        
        size = 2 * size

def calculate_min_run(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r

# Example usage:
arr = [5, 21, 7, 23, 19]
tim_sort(arr)
print(arr)  # Output: [5, 7, 19, 21, 23]

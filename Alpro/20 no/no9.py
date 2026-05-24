def missing(arr):
    n = len(arr)
    d = (arr[-1] - arr[0]) // n
    def search(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        if arr[mid] == arr[0] + mid * d:
            return search(mid + 1, hi)         
        
        if mid == 0 or arr[mid-1] == arr[0] + (mid-1) * d:
            return arr[0] + mid * d
        return search(lo, mid - 1)
    return search(0, n - 1)

print(missing([10, 15, 20, 30, 35]))  
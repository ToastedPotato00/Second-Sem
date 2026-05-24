def countZero(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr)
    if lo == hi:
        return len(arr) - lo          
    mid = (lo + hi) // 2
    if arr[mid] == 0:
        return countZero(arr, lo, mid)      
    else:
        return countZero(arr, mid + 1, hi)  
    
print(countZero( [1, 1, 0, 0, 0, 0, 0]))
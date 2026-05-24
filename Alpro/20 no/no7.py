def issqrt(n,lo=0,hi=None):
    if hi == None:
        hi = n
    mid = (lo+hi)//2
    if mid*mid == n:
        return mid
    if hi < lo:
        return hi
    if mid*mid > n:
        return issqrt(n,lo=lo,hi=mid-1)
    if mid*mid < n:
        return issqrt(n,lo=mid+1,hi=hi)

print(issqrt(26))
def vote(n,low=0,high=None):
    if high == None:
        high = len(n)-1
    if high == low:
        return n[high]
    mid = (high+low)//2
    l = vote(n,low=low, high=mid)
    r = vote(n,low=mid+1,high=high)

    if l == r:
        return l
    else:
        l_count = 0
        r_count = 0
        for i in range(low,high+1):
            if n[i] == l:
                l_count+=1
            elif n[i] == r:
                r_count+=1
        if l_count > r_count:
            return l
        else:
            return r
        
print(vote([3, 2, 3, 3, 3, 3, 2]))




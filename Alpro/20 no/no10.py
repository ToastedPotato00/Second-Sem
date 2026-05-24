def lcp(strs):
    def common(a, b):
        i = 0
        while i < min(len(a), len(b)) and a[i] == b[i]:
            i += 1
        return a[:i]
    def divide(lo, hi):
        if lo == hi: 
            return strs[lo]
        mid = (lo + hi) // 2
        return common(divide(lo, mid), divide(mid+1, hi))
    return divide(0, len(strs)-1) if strs else ""

print(lcp(["sistem", "siswa", "sisi"]))
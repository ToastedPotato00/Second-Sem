def calc(a,b,result=0):
    if b == 0:
        return result
    result += a
    return calc(a,b-1,result)

print(calc(6,4))
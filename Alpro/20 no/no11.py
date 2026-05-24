def generateParens(n):
    result = []
    def bt(s, o, c):
        if len(s) == 2*n:
           return result.append(s)
        if o < n:   
            bt(s + '(', o + 1, c)
        if c < o:   
            bt(s + ')', o, c + 1)
    bt("", 0, 0)
    return result

print(generateParens(3))

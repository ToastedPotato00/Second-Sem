def letterCombos(digits):
    if not digits: 
        return []
    M = {'2':'abc','3':'def','4':'ghi','5':'jkl',
         '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    out = []
    def bt(i, cur):
        if i == len(digits):
            return out.append(cur)
        
        for ch in M[digits[i]]:
            bt(i+1, cur + ch)
    bt(0, "")
    return out

print(letterCombos("23"))

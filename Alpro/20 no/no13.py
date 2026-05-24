def restoreIP(s):
    out = []
    def bt(start, parts):
        if len(parts) == 4:
            if start == len(s): 
                out.append('.'.join(parts))
            return
        for L in (1, 2, 3):
            if start + L > len(s): 
                break
            seg = s[start:start+L]
            if (len(seg) > 1 and seg[0] == '0') or int(seg) > 255:
                continue
            bt(start + L, parts + [seg])
    bt(0, [])
    return out

print(restoreIP("25525511135"))

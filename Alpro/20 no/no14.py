def seating(people, forbidden=("Andi", "Budi")):
    out, ban = [], set(forbidden)
    def bt(cur, rem):
        if not rem:
            out.append(cur[:]); return
        for i, p in enumerate(rem):
            if cur and cur[-1] in ban and p in ban and cur[-1] != p:
                continue
            cur.append(p)
            bt(cur, rem[:i] + rem[i+1:])
            cur.pop()
    bt([], people)
    return out

print(seating(["Andi","Budi","Citra"]))
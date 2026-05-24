vokal = str(input())
def cekVokal(vokal,count,jumlah):
    
    if count == len(vokal):
        return jumlah
    temp = vokal[count]
    if temp == "a" or temp == "i" or temp == "u" or temp == "e" or temp == "o":
        jumlah += 1
        return cekVokal(vokal,count+1,jumlah)
    else:
        return cekVokal(vokal,count+1,jumlah)
        
print(cekVokal(vokal,0,0))


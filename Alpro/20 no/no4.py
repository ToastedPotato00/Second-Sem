def clean(string,temp="",index=0):
    if index == len(string):
        return temp
    if string[index] == "*":
        return clean(string,temp,index+1)
    else:
        temp2 = string[index]
        return clean(string,temp+temp2,index+1)
    
print(clean("s*u*rab*aya"))
        
        
        

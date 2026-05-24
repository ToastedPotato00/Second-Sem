def aritmatika(arr,prev=0,index=0,current=True):
    if index == len(arr)-1 and current:
        return current
    elif current == False:
        return current
    if index == 0:
        prev = abs(arr[index+1]-arr[index])
    if arr[index+1] - arr[index] == prev:
        return aritmatika(arr,prev,index+1)
    else:
        return aritmatika(arr,prev,index+1,current=False)
    
print(aritmatika([3, 6, 10, 15]))
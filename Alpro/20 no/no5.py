def cekX(arr,target,index=0,count=0):
    if index == len(arr):
        return count
    if arr[index] == target:
        return cekX(arr,target,index+1,count+1)
    else:
        return cekX(arr,target,index+1,count+0)

print(cekX([4, 2, 7, 2, 9, 2],2))
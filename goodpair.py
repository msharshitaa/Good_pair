def GoodPair(arr,k):
    size=len(arr)
    for i in range(size):
        for j in range(i+1,size):
            if arr[i]+arr[j]==k:
                return True
    
    return False
    
arr=list(map(int,input().split()))
k=int(input())
print(GoodPair(arr,k))
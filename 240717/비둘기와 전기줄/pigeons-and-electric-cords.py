n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
pig=[-1]*(n+1)

cnt=0
for num,road in arr:
    if pig[num]==-1:
        pig[num]=road
    else:
        if pig[num]!=road:
            cnt+=1
print(cnt)
n=int(input())
arr=[list(map(int,input().split())) for _ in range(2)]

move=0
for i in range(n):
    move+=arr[0][i]-arr[1][i]
    if i ==n-1:
        break
    arr[0][i+1]+=arr[0][i]-arr[1][i]
print(move)
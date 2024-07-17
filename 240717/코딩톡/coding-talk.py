n,m,p=map(int,input().split())

people=[0]*26
arr=[]
for i in range(m):
    man,num=input().split()
    arr.append([man,int(num)])

for i in range(p-1,m):
    people[ord(arr[i][0])-65]=1

for i in range(n):
    if people[i]==0:
        print(chr(i+65), end=' ')
x=int(input())

total=0
v=1
time=0
while True:
    total+=v
    time+=1
    v+=1
    if total*2==x:
        ans=time*2
        break
    if total*2>x:
        ans=(time-1)*2+1
        break
print(ans)
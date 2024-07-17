x=int(input())

total=0
v=1
time=0
while True:
    total+=v
    time+=1
    v+=1
    if total*2>x:
        break
print(time*2)
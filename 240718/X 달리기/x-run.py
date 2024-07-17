x=int(input())

def min_dis(n):
    sum_num=0
    for i in range(1,n+1):
        sum_num+=i
    return sum_num
#n이 포함

total=0
v=1
time=0
while True:
    time+=1
    total+=v
    if total+min_dis(v+1)<x:
        v+=1
    elif total+min_dis(v+1)==x:
        ans=time*2+1
        break
    elif total+min_dis(v+1)>x:#유지혹은감소
        if total+min_dis(v)<x:
            continue
            #유지
        elif total+min_dis(v)==x:
            ans=time+1
            break
        elif total+min_dis(v)>x:
            v-=1
print(ans)
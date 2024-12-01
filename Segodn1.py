a=int(input())
prost=0
neprost=0
ch=0
nada=1
while a !=0:
    for i in range(a):
        if a%nada == 0:
            ch+=1
        nada+=1
    if ch==2:
        prost+=1
    else:
        neprost+=1
    ch=0
    nada=1
    a=int(input())
print('Простых: ', prost)
print('Других: ', neprost)
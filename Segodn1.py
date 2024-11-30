a=int(input())
dva,dry=0,0
while a !=0:
    if 9<a<100 and a>0 and a%5==0:
        dva+=1
    else:
        dry+=1
    a=int(input())
print('Двухзначные, оканчиваются на 5: ', dva)
print('Других: ', dry)
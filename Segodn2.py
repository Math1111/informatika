a=int(input())
dva=0
dry=0
while a !=0:
    if 9<a<100 and a>0:
        dva+=1
    else:
        dry+=1
    a=int(input())
print('Двухзначные: ', dva)
print('Других: ', dry)
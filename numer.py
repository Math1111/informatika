k,m=map(int, input("k, m: ").split())
xa,ya=map(int, input("xa, ya: ").split())

if ya==k/xa+m:
    print("Точка лежит на прямой")
elif ya>k/xa+m:
    print("Точка лежит над прямой")
else:
    print("Точка лежит под прямой")


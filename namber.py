x=int(input("x:"))
y=int(input("y:"))
x1=x
if x>y:
    x=y  
    y=x1
print(f"x={x},y={y}")
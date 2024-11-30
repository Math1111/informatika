print ('Подсчёт цифр в числе')
n = int(input('Введите число n>>'))
k = 0
sum=0
while n != 0:
    sum+=n%10
    n = n // 10
    k += 1

print ('k=', k)
print ('Сумма цифр:', sum)

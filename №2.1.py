n1=int(input("Введите первое число: "))
n2=int(input("Введите второе число: "))
n3=int(input("Введите третье число: "))
c= (n1==n2)+(n1==n3)+(n2==n3)
if c==1:
    print ('количество совпадающих чисел=2')
elif c>=2:
    print('количество совпадающих чисел=3')
else:
    print('количество совпадающих чисел=0')
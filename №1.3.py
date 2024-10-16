n1=float(input("Введите первое число:"))
n2=float(input("Введите второе число:"))
c= (n1>n2)*n1 + (n1<n2)*n2
if c==n1:
    print(int(c))
elif c==n2:
    print (int(c))
else:
    print("Числа равны")
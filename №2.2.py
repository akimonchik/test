x1=int(input('Номер столбца первой координаты'))
y1=int(input('Номер строки первой координаты'))
x2=int(input('Номер столбца второй координаты'))
y2=int(input('Номер строки первой координаты'))
c=(x1==x2)+(y1==y2)
if c==1:
    print('YES')
else:
    print('NO')


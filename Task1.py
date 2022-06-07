numA = int(input('Введите десятичное число: '))
numB = ''
while numA > 0:
    numB = str(numA % 2) + numB
    numA = numA // 2
print(numB)
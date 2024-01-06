num = (input('Введите двузначное число: '))

if len(num) != 2 or not num.isdigit():
    print('ERROR')
else:
    print(num[0])
    print(num[1])
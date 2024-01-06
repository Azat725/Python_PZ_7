num = (input('Введите трезначное число: '))

if len(num) != 3 or not num.isdigit():
    print('ERROR')
else:
    print(num[0])
    print(num[1])
    print(num[2])
    summary = int(num[0]) + int(num[1]) + int(num[2])
    print(summary)
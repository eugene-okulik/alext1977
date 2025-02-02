secret_number = 10

while True:
    number = int(input('Угадайте число: '))
    if number == secret_number:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')

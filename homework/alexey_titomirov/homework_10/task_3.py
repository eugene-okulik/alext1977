def calc_me(func):

    def wrapper(first, second):
        if first < 0 or second < 0:
            operate = '*'
        elif first > second:
            operate = '-'
        elif second > first:
            operate = '/'
        else:
            operate = '+'

        return func(first, second, operate)

    return wrapper


@calc_me
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        return 'Error'


first_num = float(input('First number: '))
second_num = float(input('Second number: '))
result = calc(first_num, second_num)
print(f'Result: {result}')

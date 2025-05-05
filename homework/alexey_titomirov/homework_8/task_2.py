import sys

def fibonacci_numbers():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


sys.set_int_max_str_digits(0)
count = 1
for number in fibonacci_numbers():
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
        break
    count += 1

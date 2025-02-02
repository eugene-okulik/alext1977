# сначала сделал так
# words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

# for key, value in words.items():
#     print(key * value)

# но так как это решение не по теме лекции, переделал с функцией

def print_key(key_func, value_func):
    print(key_func * value_func)


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, value in words.items():
    print_key(key, value)

my_dict = {'tuple': (True, 'road', 1, None, 3.57),
           'list': [7, None, 'way', 2.42, False],
           'dict': {'one': 'value1', 'two': 'value2', 'three': 'value3', 'four': 'value4', 'five': 'value5'},
           'set': {3, 6, None, 'text', False, 1.79, 8}
           }

# pgitrint last element in 'tuple'
print(my_dict['tuple'][-1])

# add 555 in 'list'
my_dict['list'].append(555)
# delete second element in 'list'
my_dict['list'].pop(1)

# add element in 'dict'
my_dict['dict'][('i am a tuple',)] = (12, False, 'example string', 16.31)
# delete elements in 'dict'
del my_dict['dict']['three']
my_dict['dict'].pop('two')

# add element in 'set'
my_dict['set'].add('next_element')
# delete element in 'set'
my_dict['set'].discard(1.79)

print(my_dict)

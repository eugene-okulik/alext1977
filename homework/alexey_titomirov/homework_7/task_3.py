def create_number(result_string):
    index_number = result_string.index(':') + 2
    number = int(result_string[index_number:]) + 10
    return number


result_operation_1 = 'результат операции: 42'
result_operation_2 = 'результат операции: 514'
result_program = 'результат работы программы: 9'

summ = create_number(result_operation_1) + create_number(result_operation_2) + create_number(result_program)

print(summ)

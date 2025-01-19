# initial data
result_operation_1 = 'результат операции: 42'
result_operation_2 = 'результат операции: 514'
result_program = 'результат работы программы: 9'

# create numbers
index_number_1 = result_operation_1.index(':') + 2
number_1 = int(result_operation_1[index_number_1:]) + 10

index_number_2 = result_operation_2.index(':') + 2
number_2 = int(result_operation_2[index_number_2:]) + 10

index_number_3 = result_program.index(':') + 2
number_3 = int(result_program[index_number_3:]) + 10

# print sum
summ = number_1 + number_2 + number_3
print(summ)

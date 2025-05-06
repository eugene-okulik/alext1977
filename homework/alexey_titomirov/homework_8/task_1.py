import random

salary = int(input('Input your salary: '))
bonus_variant = [True, False]
bonus = random.choice(bonus_variant)
full_salary = salary
if bonus:
    full_salary += int(random.random() * 1000)
print(f"{salary}, {bonus} - '${full_salary}'")

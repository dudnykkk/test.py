# name = input("Введите своё имя: ")
# salary = int(input("Введите свою зарплату: "))

# year_wage = int(salary * 0.3 * 12)

# print(f'{name}, за год твои накопления составят {year_wage}')

# if year_wage >= 200000:
#     print("У тебя хорошая зарплата, с возможностью накопления.")
# else:
#     print("Низкая зарплата для проживания в Чехии")


# while True:
#     print("1 - Расчитать кол-во накоплений")
#     print("2 - Завершить и выйти")

#     choice = input("Введите число: ")

#     if choice == "1":
#         name = input("Введите свое имя: ")
#         wage = int(input("Введите вашу зарлату: "))
    
#         year_salary = int(wage * 0.3 * 12)
#         print(f'name, кол-во ваших накоплений за год составит: {year_salary}')

#     elif choice == "2":
#             print("Вы успешно вышли из расчета.")
#             break
#     else:
#          print("Неверный выбор")


# name = input("Введите своё имя: ")
# salary = int(input("Введите свою зарплату: "))
# percent = int(input("Введите кол-во процентов для накоплений от доходов:"))
# goal = int(input("Ваша цель: "))

# monthly_save = salary * percent / 100
# months = round(goal / monthly_save)

# print(f'{name}, с вашим месячным доходом, вам понадобится {months} месяц(ев), чтобы накопить {goal} ')

        #26.02.25 задание от GPT
# Пользователь вводит:
# имя
# зарплату в месяц
# процент накоплений
# финансовую цель
# Программа должна:
# посчитать сколько откладывается в месяц
# посчитать сколько месяцев нужно\
# посчитать сколько лет и месяцев это будет
# И вывести красиво:

user_name = input("Введите своё имя: ")
user_salary = int(input("Введите свою месячную зарплату: "))
percent = int(input("Введите кол-во процентов накоплений: "))

while percent < 0 or percent > 100:
    print("Ошибка, процент должен быть указан от 1 до 100")
    percent = int(input("Введите кол-во процентов накоплений снова: "))
    
goal = int(input("Введите вашу финансовую цель: "))
months_save = user_salary * percent / 100
months_goal = goal / months_save
years = int(months_goal // 12)
remaining_month = round(months_goal % 12)

print(f"{user_name}, здраствуйте! При накоплениях {percent}%. Вы откладываете {months_save} в месяц.")
print(f"Вам понадобится примерно {int(months_goal)} месяц(ев)")
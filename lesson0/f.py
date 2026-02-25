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


name = input("Введите своё имя: ")
salary = int(input("Введите свою зарплату: "))
percent = int(input("Введите кол-во процентов для накоплений от доходов:"))
goal = int(input("Ваша цель: "))

monthly_save = salary * percent / 100
months = round(goal / monthly_save)

print(f'{name}, с вашим месячным доходом, вам понадобится {months} месяц(ев), чтобы накопить {goal} ')
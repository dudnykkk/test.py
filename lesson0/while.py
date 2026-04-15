# secret = 7
# attempts = 5
# while True:
#     try:
#         guess = int(input("Угадайте число от 1 до 10: "))
#         if guess > secret:
#             print("Ты ввел больше, попробуй снова")
#         elif guess < secret:
#             print("Ты ввел меньше, попробуй снова")
#         else:
#             print("Ты угадал - молодец!")
#             break

#         attempts -= 1
#     except ValueError:
#         print("Это не число, пробуй снова")
#         attempts -=1


# count = 0
# for i in range(1, 11):
#     if i > 6:
#         count += 1
#         print(i)
# print("Таких чисел:" , count)


# attempts = 5

# while attempts > 0:
#     number = int(input("Угадайте число:"))

#     if number != 10:
#         print("Неправильное число")
    
#     elif number == 10:
#         print("Правильно")
#         break
#     else:
#         print("Неправильно")
#     attempts -= 1


# name = input("Введите своё имя: ")
# salary = int(input("Введите вашу зарплату:  "))
# print(f"{name}, если ты будешь откладывать половину от {salary} целый год. Через год у тебя будет {salary * 6} ")


while True:
    salary = input("Введи свою зарплату: ")

    if salary.isdigit():
        salary = int(salary)
        result = salary * 0.3
        print("30% от зарплаты =", result)
        break
    else:
        print("Введи только число")

while True:
    salary = input("Введи свою зарплату: ")

    if salary.isdigit():
        salary = int(salary)

        tax = salary * 0.15
        expenses = salary * 0.4
        savings = salary * 0.2

        remaining = salary - tax - expenses - savings

        print("Налог:", tax)
        print("Расходы:", expenses)
        print("Сбережения:", savings)
        print("Остаток:", remaining)

        break
    else:
        print("Введи только число!")
# temperature = float(input("Enter temperature:"))
# if temperature < 0:
#     print("Freezeling")
# elif temperature >= 0 and temperature <= 20:
#     print("Warm")
# else:
#     print("Hot")


# age = int(input("Enter your age:"))
# if age < 12:
#     print("Child")
# elif age == 12 and age <= 17:
#     print("Teen")
# elif age >= 18 and age <=64:
#     print("Adult")
# elif age >= 65 and age <=100:
#     print("Senior")
# else:
#     print("Неккоректно указан возраст")


# fromto = int(input("Enter num:"))
# if fromto >= 5 and fromto <= 20:
#     print("В диапазоне")
# else:
#     print("Вне диапазона")

while True:

    salary = input("Введите свою зарплату: ")

    if salary.isdigit():
        salary = int(salary)
        if salary > 0:
            break
        else:
            print("Зарплата не может быть меньше 0")
    else:
        print("Enter salary")

if salary <= 30000:
    bonus = salary * 0.1
elif salary <= 50000:
    bonus = salary * 0.2
else:   
    bonus = salary * 0.3

total = salary + bonus
print(f"Твоя зарплата и бонус составляет: {total}")

while True:
    temp = input("Введите температуру: ")

    if temp.lstrip("-").isdigit():
        temp = int(temp)
        break
    else:
        ("Введите температуру!")

if temp > 8:
    print("Высокая температура!")
elif temp >= 2:
    print("Температура в норме")
elif temp < 2:
    print("Низкая температура")
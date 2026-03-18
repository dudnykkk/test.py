
# for i in range(1, 31):
#     if i % 3 == 0:
#         print(f"Число делится на 3: {i}" )

# sum = 0

# for i in range (1, 31):
#     if i % 3 == 0:
#         sum = sum + i
#         print(sum)



# for i in range(1, 51):

#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
# else:
#     print(i)


# n = int(input("Введите число: "))

# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")


salary = int(input("Введите зарплату: "))
expenses = int(input("Введите расходы: "))

lost = salary - expenses
print(f"Остаток: {lost}")

if lost > 10000:
    print("Ты красавчик")
elif lost >= 0:
    print("Нормально")
else:
    print("У тебя будет долг")

salary = int(input("Введите зарплату: "))
expenses = int(input("Введите расходы: "))

lost = salary - expenses
print(f"Остаток: {lost}")

if lost > 10000:
    print("Ты красавчик ")
elif lost >= 0:
    print("Нормально ")
elif lost >= -20000:
    print("У тебя будет долг ")
else:
    print("КРИТИЧНО ")
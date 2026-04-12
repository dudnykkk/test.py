# numbers = [1,2,3,4]
# for n in numbers:
#     print(n)

# for i in range(6):
#     print(i)


# for i in range(2, 6):
#     print(i)


# numbers = [5, 12, 8, 20, 3]

# for n in numbers:
#     if n > 10:
#         print(n)


#завтра повторить и использовать больше с if elif else

# total = 0
# for i in range(1, 101):
#     total = total + i
# print(total)
# расчет чисел идет суммирования к каждому числу

# for day in range(1, 6):
#     print("Рабочий день:", day)

# for i in range(1, 11):
#     print(f"Число: {i} " )

# total = 0

# for i in range(1, 11):
#     total = total + i

# print(total)

# for i in range(1, 11):
#     result = i * 2
#     print(result)\

# for i in range(1, 6):
#     print(i, "->", i*i)

# total = 0

# for i in range(1, 6):
#     print(3 * i)


# 09.03!!!


# for i in range(5, 26, 5):
#     print(i)

# for i in range(1, 6):
#     print(f"{i} * 3 = {i*3}")

# for i in range (2, 11, 2):
#     print(i)


# for i in range (2, 21):
#     if i % 2 == 0:
#         print(f"{i} Это четное число!")
#     elif i % 2 == 1:
#         print(f"{i} Нечетное число")

# total = 0
# for i in range(1, 11):
#     total = total + i
#     print(total)


#COUNTER!!!!!!!!!! 10.03

# counter = 0
# for i in range(1, 11):
#     if i % 2 == 0:
#         counter = counter + 1
# print(counter)

# counter = 0
# for i in range(1, 21):
#     if i % 2 == 1:
#         counter += 1
# print(f"Total: {counter}")


# counter = 0
# for i in range(1, 21):

#     if i % 2 == 1:
#         print(i)
#         counter += 1
# print(f"Total: {counter}")


# numbers = [3, 7, 12, 5, 9]

# for n in numbers:
#     print(n)



# numbers = [2, 4, 5, 7, 12, 13, 17, 14, 22]
# for n in numbers:
#     if n % 2 == 0:
#         print(n)


# numbers = [1, 2, 3, 4, 5]

# for n in numbers:
#         print(n * 2)


# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     if n > 3:
#           print(n)



# total = 0
# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     total = total + n

# print(total)

# average = 0
# total = 0
# salaries = [1000, 1200, 1500, 2000, 800]

# for i in salaries:
#     total = total + i
# print(f"Total: {total}")

# for i in salaries:  
#     if i >= 1200:
#         print(i)

# average = total / len(salaries)
# print(f"Average: {average}")

# salary = int(input("Enter salary: "))

# if salary >= 1500:
#     print("Хорошая зарплата")
# elif salary >= 1000 and salary <= 1500:
#     print("Достаточная зарплата")
# else:
#     print("Недостаточно денег для покрытия базовых потребностей")

count = int(input("How many: "))
average = 0
total = 0

for i in range(count):
    s = int(input("Enter salary: "))
    total = total + s

average = total / count
print(f"Total: {total}")
print(f"Average: {average}")


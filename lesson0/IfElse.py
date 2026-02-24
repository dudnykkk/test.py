temperature = float(input("Enter temperature:"))
if temperature < 0:
    print("Freezeling")
elif temperature >= 0 and temperature <= 20:
    print("Warm")
else:
    print("Hot")


age = int(input("Enter your age:"))
if age < 12:
    print("Child")
elif age == 12 and age <= 17:
    print("Teen")
elif age >= 18 and age <=64:
    print("Adult")
elif age >= 65 and age <=100:
    print("Senior")
else:
    print("Неккоректно указан возраст")


fromto = int(input("Enter num:"))
if fromto >= 5 and fromto <= 20:
    print("В диапазоне")
else:
    print("Вне диапазона")


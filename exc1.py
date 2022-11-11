weekDay = input("Input a number: ")
if weekDay == '6' or weekDay == '7':
    print("it is weekend")
else:
    print("Not a weekend")


# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
predicVal = [True, False]
for x in predicVal:
    for y in predicVal:
        for z in predicVal:
            if not (x == True or y == True or z == True) == (x != False and y != False and z != False):
                print("x=", x, "y=", y, "z=", z, ".",
                      "Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно!")
            else:
                print("x=", x, "y=", y, "z=", z, ".",
                      "Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно!")

# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def DetermineQuarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3
    else:
        return 4

x = int(input("Введите x: "))
y = int(input("Введите y: "))
print("Четверть №",DetermineQuarter(x ,y))
print('AGE is', 20)
print("addition,2+3")
print("subtraction,2-3")
print("division,2/3")
print("multiplication,2*3")

a = 10
b = 20
c = a + b
print('Addition of A+B ', c)
# print('Subtraction of A-B',c)
# print('Division of A/B',c)
# print('Multplication of A*B',c)

a = int(input("Enter first integer"))
b = int(input("Enter second integer"))
print('Addition of A+B ', a + b)
print('subtraction of A-B', a - b)
print('divsion of A/B', a / b)
print('multiplication of A*B', a * b)
a = 10
b = 20
c = 30
print('average of A+B+C/3', a + b + c / 3)

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

if num1 == 0:
    print("Cannot divide by zero.")
elif num2 % num1 == 0:
    print("The second number is a multiple of the first.")
else:
    print("The second number is not a multiple of the first.")

while 1 > 0:
    print("Welcome ")
i = 0
while i < 1000:
    print("Welcome")
    i = i = 1
i = 0
while i < 1000:
    if i % 2 == 0:
        print('Even', i)
    # i = i + 1
    i += 1

for value in range(0, 1000):
    if value % 2 == 0:
        print("Even", value)
    else:
        print("Odd", value)
fruits = ("apple", "banana", "cherry")
for x in fruits:
    if (x == "banana"):
        print(x)


        def printvalue():
            print('Welcome')

printvalue()


def addvalue(a, b):
    return a + b


val = addvalue(a=3, b=4)
print(val)
if 1 > 2:
    print("five is geater than two!")
    print("5>2")

    print("not if block")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)


def check_age():
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are of legal age.")
    else:
        print("You are not of legal age.")


check_age()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)

for i in range(1, 11):
    print(i)

for i in range(1, 101):
    if i % 2 == 0:
        print(i)

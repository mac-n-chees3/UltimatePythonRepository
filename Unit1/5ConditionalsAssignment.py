
print("########## 1.5.1 ##########")
number = int(input("Please type a number: "))
if number == 1984:
    print("Orwell")
print("########## 1.5.2 ##########")
number = int(input("Please type in a number: "))
if number < 0:
    av = number*-1
    print("The absolute value of this number is", av)
if number > 0:
    print("The absolute value of this is", number)
print("########## 1.5.3 ##########")
cost = 5.90
name = input("What is your name? ")
if name == str("Jerry"):
    print("Next please!")
if name != str("Jerry"):
    portion = int(input("How many portions of soup? "))
    total = cost*portion
    print("The total cost is", total)
    print("Next please!")
print("########## 1.5.4 ##########")
number = int(input("Type in a number: "))
if number < 1000:
    print("This number is smaller than 1000")
if number < 100:
    print("This number is less than 100")
if number < 10:
    print("This number is less than 10")
print("Thank you!")
print("########## 1.5.5 ##########")
number = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")
if operation == str("add"):
    add = number+number2
    print(number, "+", number2, "=", add)
if operation == str("multiply"):
    multiply = number*number2
    print(number, "*", number2, "=", multiply)
if operation == str("subtract"):
    subtract = number-number2
    print(number, "-", number2, "=", subtract)
print("########## 1.5.6 ##########")
temperature = int(input("Type in a temperature (F): "))
celsius = (temperature-32) * 5/9
print(temperature, "degrees Fahrenheit equals", celsius, "degrees Celsius")
if celsius < 0:
    print("Brr! It's cold in here!")
print("########## 1.5.7 ##########")
wage = float(input("What is your hourly wage? "))
hours = float(input("How many hours have you worked? "))
day = input("What day of the week is it? ")
if day != str("Sunday"):
    dailywage = wage*hours
    print("daily wages:", dailywage)
if day == str("Sunday"):
    dailywage = (wage*2)*hours
    print("daily wage:", dailywage)
print("########## 1.5.8 ##########")
# Fix the program
points = int(input("How many points are on your card? "))
if points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")
if points < 100:
    points *=1.1
    print("Your bonus is 10 %")

print("You now have", points, "points")

print("########## 1.5.9 ##########")
print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
if temperature > 20:
    print("Wear jeans and a T-shirt")
if temperature <= 20:
    print("Wear jeans and a T-shirt")
    print("I reccommend a sweater as well")
if temperature <= 10:
    print("take a jacket with you")
if temperature <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == str("yes"):
    print("Don't forget your umbrella!")
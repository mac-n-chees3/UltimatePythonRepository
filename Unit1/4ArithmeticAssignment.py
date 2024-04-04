print("########## 1.4.1 ##########")
#Write a code which asks the user for a number. 
#The program then prints out the number multiplied 
#by five.
number_str = (input("enter a number here: "))
number = int(number_str)
number2 = 5
sum = number*number2
print(number, "times", number2, "is", sum)
print("########## 1.4.2 ##########")
#Write code which asks the user for their name and
#year of birth.
name = input("What is your name? ")
year_born = input("which year were you born? ")
year = int(year_born)
current_year = 2024
age = (current_year-year)
print("hello", name + ",", "you will be", age, "at the end of the year 2024")
print("########## 1.4.3 ##########")
#Write code which asks the user for a number of days.
#The code then prints out the number of seconds in 
# the amount of days given.
days_gone_by = input("How many days? ")
days = int(days_gone_by)
seconds = 86400
seconds_in_day = (seconds*days)
print("Seconds in that many days:", seconds_in_day)
print("########## 1.4.4 ##########")
# Fix the code
number = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
product = number * number2 * number3

print("The product is", product)

print("########## 1.4.5 ##########")
number = int(input("enter first number: "))
number2 = int(input("enter second number: "))
sum = number + number2
product = number * number2
print("the sum of ther numbers:", sum)
print("the product of the numbers:", product)
print("########## 1.4.6 ##########")
number = int(input("number 1: "))
number2 = int(input("number 2: "))
number3 = int(input("number 3: "))
number4 = int(input("number 4: "))
sum = number + number2 + number3 + number4
mean = sum / 4
print("The sum of the numbers is", sum, "and the mean is", mean)
print("########## 1.4.7 ##########")
schoolLunch = float(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))
total_spent = groceries + schoolLunch * price
daily = total_spent/ 7
weekly = daily* 7
print("Average food expenditure:")
print("Daily:", "$" + daily)
print("Weekly:", "$" + weekly)

print("########## 1.4.8 ##########")


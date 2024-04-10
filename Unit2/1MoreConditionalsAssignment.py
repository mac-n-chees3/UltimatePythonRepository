print("########## 2.1.1 ##########")
word = (input("enter word here: "))
if (len(word)) == 1:
 print("Thank you!")
elif (len(word)) > 1:
 print(len(word))   
 print("Thank you!")
print("########## 2.1.2 ##########")
temperature = float(input("Please type in a temperature: "))
integer = int(temperature)
decimal = round(temperature-integer, 2)
print("Integer part:", integer)
print("Decimal part:", decimal)
print("########## 2.1.3 ##########")
age = int(input("How old are you? "))
if age <= 18:
    print("You may not vote.")
else:
    print("You may vote!")
print("########## 2.1.4 ##########")
number = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
if number > number2:
    print("The greater number was:", number)
elif number < number2:
    print("The greater number was:", number2)
else:
    print("The numbers are equal!")
print("########## 2.1.5 ##########")
name = (input("What is your name? "))
age = int(input("What is your age? "))
name2 = (input("What is your name? "))
age2 = int(input("What is your age? "))
print("Person 1:")
print("Name:", name)
print("age:", age)
print("Person 2:")
print("Name:", name2)
print("age:", age2)
if age > age2:
    print("the elder is", name)
elif age < age2:
    print("the elder is", name2)
else:
    print(name, "and", name2, "are the same age")
print("########## 2.1.6 ##########")
word = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")
if word > word2:
    print(word, "comes in alphabetically last.")
elif word < word2:
    print(word2, "comes alphabetically last.")
else:
    print("You gave the same word twice.")

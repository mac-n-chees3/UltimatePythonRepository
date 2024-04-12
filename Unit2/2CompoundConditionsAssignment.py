print("########## 2.2.1 ##########")
age = int(input("What is your age? "))
if age <= 0:
    print("That must be a mistake")
else: 
    if age < 5:
        print("I suspect you can't write quite yet...")
    else:
        print("Ok, you're", age, "years old")
print("########## 2.2.2 ##########")
name = input("please type in your name: ")
if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of")
print("########## 2.2.3 ##########")
percent = int(input("Type in percent: "))
if percent < 0:
    print("Impossible!")
elif percent >= 0 and percent <= 59:
    print("Grade: F")
elif percent >= 60 and percent <= 69:
    print("Grade: D")
elif percent >= 70 and percent <= 79:
    print("Grade: C")
elif percent >= 80 and percent <= 89:
    print("Grade: B")
elif percent >= 90 and percent <= 100:
    print("Grade: A")
else:
    print("impossible!")
print("########## 2.2.4 ##########")
number = int(input("Number: "))
if number % 3 == 0 and number %5 ==0:
    print("fizzbuzz")
else:
    if number %3==0:
        print("fizz")
    elif number%5==0:
        print("buzz")
print("########## 2.2.5 ##########")
year = int(input("Please type in a year: "))
if year % 100 == 0:
    print("That year is not a leap year")
else:
    if year % 4 == 0:
        print("that year is a leap year")
    else:
        print("that is not a year")
print("########## 2.2.6 ##########")
l1 = input("1st letter: ")
l2 = input("2nd letter: ")
l3 = input("3rd letter: ")
if l1 > l2 and l1 < l3:
    print("The letter in the middle is", l1) 
elif l1 < l2 and l1 > l3:
    print("the letter in the middle is", l1)
elif l2 > l1 and l2 < l3:
    print("the letter in the middle is", l2)
elif l2 < l1 and l2 < l3:
    print("the letter in the middle is", l2)
elif l3 > l1 and l3 < l2:
    print("the letter in the middle is", l3)
elif l3 <l1 and l3 > l2:
    print("the letter in the middle is", l3)
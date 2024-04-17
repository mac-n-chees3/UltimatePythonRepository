# ========== 2.3.1 ==========
# while True:
#     print("hi")
#     text = input("Shall we continue? ")
#     if text == "no":
#         print("okay then")
#         break
# ========== 2.3.2 ==========
# while True:
#     number = int(input("Please type in a number: "))
#     if number < 0:
#         print("invalid number")
#     elif number == 0:
#         print("exiting...")
#         break
#     elif number > 0:
#         from math import sqrt 
#         print(sqrt(number))
# ========== 2.3.3 ==========
# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number < 0:
#     break

# print("Now!")

# ========== 2.3.4 ==========
# password = input("Password: ")
# while True:    
#     rp = input("Repeat password: ")
#     if rp != password:
#         print("They do not match!")
#     elif rp == password:
#         print("User account created!")
#         break
# ========== 2.3.5 ==========
# attempts = 0
# while True:
#     code = "4321"
#     pin = (input("PIN: "))
#     if pin != code:
#         success = False
#         print("Wrong")
#         attempts += 1
#     else:
#         success = True
#         break
# if success:
#     if attempts < 1:
#         print("Correct! It only took you one try!")
#     elif attempts >= 1:
#         print("Correct!, it took you", (attempts+1), "tries")
# ========== 2.3.6 ==========
# year = int(input("Year: "))
# r = 0
# while True:
#     r = year%4
#     leapyear = year-r+4
#     print("The next leap year after", year, "is", leapyear)
#     break
# ========== 2.3.7 ==========
# words = ""
# while True:
#     word = input("Please type in a word: ")
#     if word != "end":
#         end = False
#         words += word + " "
#     else:
#         print(words)
#         break
# ========== 2.3.8 ==========
# words = ""
# recentword = ""
# while True:
#     word = input("Please type in a word: ")
#     if word == "end":
#         print(words)
#     elif recentword == word:
#         print(words)
#         break
#     else:
#         word != "end"
#         recentword = word
#         words += recentword + " "
# ========== 2.3.9 ==========
print("Please type in integer numbers. Type in 0 to finish.")
totalnumbers = 0
sumofnumbers = 0
meanofnumbers = 0
positive = 0
negative = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        print("Numbers typed in:", totalnumbers)
        print("Sum of numbers:", sumofnumbers)
        print("Mean of numbers:", meanofnumbers)
        print("Positive numbers:", positive)
        print("Negative numbers:", negative)
    else:
        totalnumbers += 1
        sumofnumbers += number
        meanofnumbers = sumofnumbers/totalnumbers
        if number % 2 == 0:
            positive += 1
        else:
            negative += 1
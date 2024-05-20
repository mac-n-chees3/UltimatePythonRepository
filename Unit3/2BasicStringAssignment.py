# ========== 3.2.1 ==========
# string = input("Please type in a string: ")
# amount = int(input("Please type in an amount: "))
# total = string * amount
# print(total)
# ========== 3.2.2 ==========
# string1 = input("Please type in a string: ")
# string2 = input("Please type in string 2: ")
# if len(string1) > len(string2):
#     print(string1, "is longer")
# elif len(string2) > len(string1):
#     print(string2, "is longer")
# else:
#     print("The strings are equally long")
# ========== 3.2.3 ==========
string = input("Enter a string: ")
length = len(string)



index = -1, -2, -3, -4

index = -1
while index >= -length :
    print(string[index])
    index = index - 1

# ========== 3.2.4 ==========
# string = input("enter a string: ")
# if string[1] == string[-2]:
#     print("The second letter and the second to last letter are the same")
# else:
#     print("The second and second to last letter are different")

# ========== 3.2.5 ==========
# widith = int(input("Widith: "))
# length = '#' * widith
# print(length)
# ========== 3.2.6 ==========
# Widith = int(input("Width: "))
# height = int(input("Height: "))
# line = '#' * Widith + '\n' 
# total = height * line
# print(total)
# ========== 3.2.7 ==========
# text = ''
# while True:
#     text = input("Please type in a string: ")
#     underline = '-' * len(text)
#     print(text)
#     print(underline)
#     if text == '':
#         break
# ========== 3.2.8 ==========
# string = input("Enter a string: ")
# max = 20
# totalneed = max - len(string)
# done = totalneed * '*'
# needed = done + string
# print(needed)
# ========== 3.2.9 ==========
# word = input("insert string; ")
# max = 30
# inside = 28
# newinside = 25 - len(word)
# number_of_leftspaces = newinside // 2
# number_of_rightspaces = number_of_leftspaces
# leftspaces = " " * number_of_leftspaces
# rightspaces = " " * number_of_rightspaces
# print("******************************")
# print('*', leftspaces, word, rightspaces, '*')
# print("******************************")

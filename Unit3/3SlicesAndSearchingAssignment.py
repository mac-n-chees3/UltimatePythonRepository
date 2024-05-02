# ========== 3.3.1 ==========
# string = input("string: ")
# part = string[0:0]
# number = 0
# while len(part) < len(string):
#     part += string[number]
#     number += 1
#     print(part)
# ========== 3.3.2 ==========
# string = input("string: ")
# number = len(string) - 1
# part = string[number]
# while number >= 0:
#     part = string[number:]
#     number -= 1
#     print(part)
# ========== 3.3.3 ==========
# string = input("string; ")
# if ('a' in string) == True:
#     print('a found')
# else:
#     print('a not found')
# if ('e' in string) == True:
#     print('e found')
# else:
#     print('e not found')
# if ('o' in string) == True:
#     print('o found')
# else:
#     print('o not found')
# ========== 3.3.4 ==========
# string = input('String: ')
# character = input('Character: ')
# position = string.find(character)
# if len(string) >= 3:
#     print(string[position:position+3])
# ========== 3.3.5 ==========
# You can skip this one...
# word = input("Word: ")
# character = input('Character: ')
# position = word.find(character)
# while True:
#     if len(word) <= 2:
#         break
#     print(word)
#     word = word[position:]
#     position += 1
# ========== 3.3.6 ==========
# whole = input('String: ')
# search = input('substring: ')
# position = whole.find(search)


# part = whole[position+1:]

# newposition = part.find(search)
# if newposition == -1:
#     print("The substring does not occur twice in the string")
# else:
#     final_answer = position + newposition + 1
#     print("The second occurrence of the substring is at index", final_answer)
# ========== 4.2.1 ==========
# def greatest_number(a, b, c):
#     if a > b and a > c:
#         return a
#     elif a < b and b > c:
#         return b
#     elif c > b and c > a:
#         return c
#     else:
#         return a
# print(greatest_number(3, 4, 1))
# print(greatest_number(99, -4, 7))
# print(greatest_number(0, 0, 0))
# ========== 4.2.2 ==========
def same_chars(string, a, b):
    print(string, a, b)
    if b > len(string):
        return False
    elif string[a] == string[b]:
        return True
    elif string[a] != string[b]:
        return False
print(same_chars("programmer", 6, 7))
print(same_chars("programmer", 0, 4))
print(same_chars("programmer", 0, 12))
# ========== 4.2.3 ==========
# def first_word(word):
#     word = sentence[0:2]
#     return word
# def second_word(word2):
#     word2 = sentence[3:6]
#     return word2
# def last_word(word7):
#     word7 = sentence[25:31]
#     return word7
# sentence = 'it was a dark and stormy python'

# print(first_word(sentence))
# print(second_word(sentence))
# print(last_word(sentence))

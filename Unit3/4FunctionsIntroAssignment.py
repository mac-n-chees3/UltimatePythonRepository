# ========== 3.4.1 ==========
# def seven_dwarves():
#     print('Bashful\nDoc\nDopey\nGrumpy\nHappy\nSleepy\nSneezy')
# seven_dwarves()
# ========== 3.4.2 ==========
# def first_character(character):
#     print(character[0:1])
# first_character('python')
# first_character('yellow')
# first_character('tomorrow')
# first_character('heliotrope')
# first_character('open')
# first_character('night')
# ========== 3.4.3 ==========
# def mean(n1, n2, n3):
#     Mean = (n1 + n2 + n3) /3
#     print(f'the mean of {n1, n2, n3} is {Mean}')
# mean(5, 3, 1)
# mean(10, 1, 1)

# ========== 3.4.4 ==========
# def print_many_times(text, times):
#     lines = text + '\n'
#     row = lines * times
#     print(f'{row}')
    

# print_many_times("hi", 5)

# print()

# text = "All Pythons, except one, grow up"
# times = 3
# print_many_times(text, times)
# ========== 3.4.5 ==========
# def hash_square(length):
#     row = length
#     while row > 0:
#         print('#'*length)
#         row -= 1
# hash_square(3)
# print()
# hash_square(5)
# ========== 3.4.6 ==========
def chessboard(rows):
    count = 0
    lines = rows
    while lines > 0:
        characters = rows
        while characters > 0:
            if count % 2 == 0:
                print('1', end="")
                characters -= 1
            else:
                print('0', end='')
                characters -= 1
            count += 1
        lines -= 1
        if rows % 2 == 0:
            count-= 1
        print()
chessboard(3)
print()
chessboard(6)
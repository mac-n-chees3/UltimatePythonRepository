
# def sum(x, y):
#     added = x + y
#     print(f'the sum of {x} and {y} is', added)

# sum(4, 5)

# ========== 4.1.1 ==========

def line(integer, string):
    if len(string) == 0:
        print(integer*'*')
    else:
        print(string[0]*integer)
# line(7, '%')
# line(10, "LOL")
# line(3, "")
# ========== 4.1.2 ==========

# def square_of_hashes(height):
#     rows = height

#     while rows > 0:
#         line(10, '#')
#         rows -= 1


# square_of_hashes(5)
# print()
# square_of_hashes(2)

# ========== 4.1.3 ==========
# def box_of_hashes(length):
#     width = length
#     while width > 0:
#         line(length, '#')
#         width -= 1

# box_of_hashes(5)
# print()
# box_of_hashes(3)

# ========== 4.1.4 ==========
# def square(length, character):
#     width = length
#     while width > 0:
#         line(length, character)
#         width -= 1
# square(5, "*")
# print()
# square(3, "o")
# ========== 4.1.5 ==========
# def triangle(length):
#     width = 1 
#     string = '#'
#     while width < length + 1:
#         line(width, string)
#         width += 1
        
# triangle(6)
# print()
# triangle(3)        
# ========== 4.1.6 ==========
# def shape(w, c, h, fc):
    # do the triangle printing using w and c
    # width = 1
    # character = c 
    # while width < w + 1:
    #     line(width, character)
    #     width += 1

    # do the rectangle printing with h and fc
    # rows = h
    # while rows > 0:
    #     line(w, fc)
    #     rows -= 1

# shape(5, "X",3, "*")
# print()
# shape(2, "o", 4, "+")
# print()
# shape(3, ".", 0, ",")
# ========== 4.1.7 ==========

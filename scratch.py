# def message():
#     print('This is my very own function')
# message()


# def hello(name):
#     print('hello', name, '!')

# hello("Alice")
# hello('world')

# def squared(x):
#     print(f'The square of the number {x} is {x * x}')
# squared(2)
# squared(5)

# x = int(input('number: '))
# y=int(input('number: '))
# def sum(x, y):
#     x = int(input('number: '))
#     y=int(input('number: '))
#     result = x+y
    
#     print(f'The sum of the arguments {x} and {y} is {result}')



# Widith = int(input("Width: "))
# height = int(input("Height: "))
# line = '#' * Widith + '\n' 
# total = height * line
# print(total)

# def print_sum(a, b):
#    print("The sum of", a, "and", b, "is", a + b)

# def return_sum(a, b):
#    return a + b

# total = print_sum(3, 7)
# print("The value returned was:", total)

# total = return_sum(3, 7)
# print("The value returned was:", total)

# def smallest(a, b):
#    if a < b:
#       return a
#    return b
# smallest(3, 7)

# def greet(name):
#     print("Hello there,", name)

# def greet_many_times(name, times):
#     while times > 0:
#         greet(name)
#         times -= 1

# greet_many_times("Emily", 3)

def box_of_hashes(height):
    height = '#' + '\n'
def line(height, width):
    while len(width) < 10:
        width += '#'

box_of_hashes(5)
print()
box_of_hashes(3)
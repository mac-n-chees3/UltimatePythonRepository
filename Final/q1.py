first = input('Enter your first name: ')
last = input('Enter your last name: ')
gpa = float(input('enter your GPA: '))
if last[0] == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'K':
    if gpa < 3.25:
        print('Hello,', first + '.', 'You should report to school on Monday and Thursday. You are eligible for a scholarship of $0.')
    elif gpa >= 3.25 or gpa <= 3.49:
        print('Hello,', first + '.', 'You should report to school on Monday and Thursday. You are eligible for a scholarship of $4000.')
    elif gpa >= 3.50 or gpa <= 3.69:
        print('Hello,', first + '.', 'You should report to school on Monday and Thursday. You are eligible for a scholarship of $8000.')
    elif gpa >= 3.7 or 3.85:
        print('Hello,', first + '.', 'You should report to school on Monday and Thursday. You are eligible for a scholarship of $12000.')
    elif gpa >= 3.86:
        print('Hello,', first + '.', 'You should report to school on Monday and Thursday. You are eligible for a scholarship of $16000.')
elif last[0] == 'L' or 'M' or 'N' or 'O' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y' or 'Z':
    if gpa >= 3.86:
        print('Hello,', first + '.', 'You should report to school on Tuesday and Friday. You are eligible for a scholarship of $16000.')
    elif gpa <= 3.85:
        print('Hello,', first + '.', 'You should report to school on Tuesday and Friday. You are eligible for a scholarship of $12000.')
    elif gpa >= 3.7:
        print('Hello,', first + '.', 'You should report to school on Tuesday and Friday. You are eligible for a scholarship of $12000.')
    elif gpa <= 3.69:
        print('Hello,', first + '.', 'You should report to school on Tuesday and Friday. You are eligible for a scholarship of $8000.')
    elif gpa >= 3.5:
        print('Hello,', first + '.', 'You should report to school on Tuesday and Friday. You are eligible for a scholarship of $8000.')
    elif gpa <= 3.49:
        print('Hello,', first + '.', 'You should report to school on Tuesday and Friday. You are eligible for a scholarship of $4000.')
    elif gpa >= 3.25:
        print('Hello,', first + '.', 'You should report to school on Tuesday and Friday. You are eligible for a scholarship of $4000.')
    elif gpa < 3.25:
        print('Hello,', first + '.', 'You should report to school on Tuesday and Friday. You are eligible for a scholarship of $0.')

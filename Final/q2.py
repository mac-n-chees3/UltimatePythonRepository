due = 50
owed = due * -1
print('amount due:', due)
while True:
    owed = due * -1
    amount = int(input('insert coin: '))
    if amount == 5 or 10 or 25:
        due -= amount
        print('amount due:', due)
        if due == 0:
            break
        elif due < 0:
            print('Change owed:', owed)
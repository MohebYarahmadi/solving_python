# DMOJ problem wc17c3j3, Uncrackable 
password = input()

digit, upper, lower = 0, 0, 0

if not (8 <= len(password) <= 12):
    print('Invalid')
else:
    for char in password:
        if char.isdigit():
            digit += 1
        elif char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    if lower < 3 or upper < 2 or digit < 1:
        print('Invalid')
    else:
        print('Valid')

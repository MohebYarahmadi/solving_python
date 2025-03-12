# DMOJ problem ccc06j1, Canadian Calorie Counting

burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())
total_cal = 0

if burger == 1:
    total_cal += 461
elif burger == 2:
    total_cal += 431
elif burger == 3:
    total_cal += 420
else:
    pass

if side == 1:
    total_cal += 100
elif side == 2:
    total_cal += 57
elif side == 3:
    total_cal += 70
else:
    pass

if drink == 1:
    total_cal += 130
elif drink == 2:
    total_cal += 160
elif drink == 3:
    total_cal += 118
else:
    pass

if dessert == 1:
    total_cal += 167
elif dessert == 2:
    total_cal += 266
elif dessert == 3:
    total_cal += 75
else:
    pass

print(f'Your total Calorie count is {total_cal}.')

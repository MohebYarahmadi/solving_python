width = int(input())
extra_cheese = int(input())

if width == 3 and extra_cheese > 95:
    message = 'absolutely'
elif width == 1 and extra_cheese <= 50:
    message = 'fairly'
else:
    message = 'very'

print(f"C.C. is {message} satisfied with her pizza.")

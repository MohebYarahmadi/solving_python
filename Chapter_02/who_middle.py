# DMOJ problem ccc07j1, Who is in the Middle
first = int(input())
second = int(input())
third = int(input())

# Find the minimum number
if first < second and first < third:
    min = first
elif second < first and second < third:
    min = second
elif third < first and third < second:
    min = third

# Find the middle number
if min == first:
    if second < third:
        mid = second
    elif third < second:
        mid = third
elif min == second:
    if first < third:
        mid = first
    elif third < first:
        mid = third
elif min == third:
    if first < second:
        mid = first
    elif second < first:
        mid = second


print(mid)

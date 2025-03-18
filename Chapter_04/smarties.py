# DMOJ problem ecoo15r1p1, When You Eat Your Smarties
color_counts = {
    'orange': 0,
    'blue': 0,
    'green': 0,
    'yellow': 0,
    'pink': 0,
    'violet': 0,
    'brown': 0,
    'red': 0
}


total_time = 0

def calculate_time(color, count):
    if color == 'red':
        return count * 16
    else:
        handfuls = (count + 6) // 7  # Equivalent to math.ceil(count / 7)
        return handfuls * 13

# color_counts = {color: 0 for color in ['orange', 'blue', 'green', 'yellow', 'pink', 'violet', 'brown', 'red']}
# while True:
#     color = input().lower()
#     if color == 'end of box':
#         break
#     if color in color_counts:
#         color_counts[color] += 1
# total_time = 0
# for color in ['orange', 'blue', 'green', 'yellow', 'pink', 'violet', 'brown', 'red']:
#     total_time += calculate_time(color, color_counts[color])
# print(total_time)


for _ in range(10):
    color_counts = {color: 0 for color in ['orange', 'blue', 'green', 'yellow', 'pink', 'violet', 'brown', 'red']}
    while True:
        color = input().lower()
        if color == 'end of box':
            break
        if color in color_counts:
            color_counts[color] += 1
    total_time = 0
    for color in ['orange', 'blue', 'green', 'yellow', 'pink', 'violet', 'brown', 'red']:
        total_time += calculate_time(color, color_counts[color])
    print(total_time)

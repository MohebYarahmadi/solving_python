# DMOJ problem ccc08j2 - Do the Shuffle
# songs = input().strip().upper().split()
songs = ['A', 'B', 'C', 'D', 'E']
# print(f'debug input: {songs}')

# btn1 0 -> -1
# btn2 -1 -> 0
# btn3 01 -> 10
# btn4 print songs

while True:
    action = int(input().strip())
    # if action == 4:# Guardian
    #     break
    count = int(input().strip())
    # if count == 4:# Guardian
    #     break
    
    # Guardian
    if action == 4:
            break

    match action:
        case 1:
            for _ in range(count):
                song = songs.pop(0)
                songs.append(song)
                # print(f'debug 1: {new_list}')

        case 2:
            for _ in range(count):
                song = songs.pop()
                songs.insert(0, song)
                # print(f'debug 2: {new_list}')

        case 3:
            for _ in range(count):
                songs[0], songs[1] = songs[1], songs[0]
                # print(f'debug 3: {new_list}')

print(*songs)

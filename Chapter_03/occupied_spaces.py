# DMOJ problem ccc18j2
n = int(input())
yesterday = input()
today = input()
occ = 0

for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occ += 1

print(occ)

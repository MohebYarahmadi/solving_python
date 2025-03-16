# DMOJ problem coci18c3p1, Magnus
text = input().upper()
cocis = []
# print(cocis)

cocis.append(text.count('H'))
cocis.append(text.count('O'))
cocis.append(text.count('N'))
cocis.append(text.count('I'))

c_mins = min(cocis)

# print(c_mins)
# print(len(cocis))
# print(cocis)

if c_mins <= 0:
    print(c_mins)
else:
    blocks = int((c_mins * 4) / 4)
    print(blocks)

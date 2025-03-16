# DMOJ problem coci13c3p1, Rijeci
k = int(input())
a = 1
b = 0

for i in range(1, k + 1):
    new_a = b
    new_b = a + b
    a = new_a
    b = new_b

print(a, b)

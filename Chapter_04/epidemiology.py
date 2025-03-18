# DMOJ problem ccc20j2, Epidemiology
p = int(input())    # P 100
n = int(input())    # N 5
r = int(input())    # R 3

# Day_0 > new infections 5, total infected 5
# Day_1 > new infections 5x3=15, total infected 5+15=20
# Day_2 > new infections 15x3=45, total infected 20+45=65
# Day_3 > new infections 45x3=135, total infected 65+135=200
# On Day_3, the total number of infected people exceeds P = 100, so the answer is 3

total_infected = n
new_infections = n
day = 0

while total_infected <= p:
    day += 1
    new_infections *= r
    total_infected += new_infections

print(day)

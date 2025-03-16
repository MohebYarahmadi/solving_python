# DMOJ problem ccc11s2
n_questions = int(input())
st_answers = [input().strip().upper() for _ in range(n_questions)]
t_keys = [input().strip().upper() for _ in range(n_questions)]
correct = 0

for i in range(len(t_keys)):
    if t_keys[i] == st_answers[i]:
        correct += 1

print(correct)

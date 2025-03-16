# DMOJ problem ccc11s1, English or French
def mine():
    n_line = int(input())
    lines = []
    
    s_word = 0
    t_word = 0
    
    for i in range(n_line):
        cin = input().lower()
        lines.append(cin)
    
    for line in lines:
        s_word += line.count('s')
        t_word += line.count('t')
    
    if t_word > s_word:
        print('English')
    else:
        print('French')
    

def detect_language(N, lines):
    t_count = 0
    s_count = 0
    
    for line in lines:
        t_count += line.lower().count('t')
        s_count += line.lower().count('s')
    
    if t_count > s_count:
        return "English"
    else:
        return "French"

# Read input
N = int(input())
lines = [input().strip() for _ in range(N)]

# Detect language
result = detect_language(N, lines)

# Output the result
print(result)

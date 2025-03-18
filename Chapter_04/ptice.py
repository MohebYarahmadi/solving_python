# DMOJ problem coci08c1p2, Ptice
n = int(input())    # number of questions
correct_answer = input().strip()

# Define the sequences
adrian_seq = ("ABC" * n)[:n]
bruno_seq = ("BABC" * n)[:n]
goran_seq = ("CCAABB" * n)[:n]

# Count matches - using 'Generator Expression' with sum function
adrian_matches = sum(1 for i in range(n) if adrian_seq[i] == correct_answer[i])
bruno_matches = sum(1 for i in range(n) if bruno_seq[i] == correct_answer[i])
goran_matches = sum(1 for i in range(n) if bruno_seq[i] == correct_answer[i])

# Find the maximum matches
m = max(adrian_matches, bruno_matches, goran_matches)

# Determine who achieved m matches
winners = []
if adrian_matches == m:
    winners.append("Adrian")
if bruno_matches == m:
    winners.append("Bruno")
if goran_matches == m:
    winners.append("Goran")

# Output the result
print(m)
for winner in sorted(winners):
    print(winner)


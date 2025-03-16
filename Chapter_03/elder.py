# DMOJ problem coci18c4p1, Elder
# Read the initial wizard the wand is obeying
current_wizard = input().strip()

# Read the number of duels
N = int(input())

# Initialize a set to keep track of all unique wizards the wand has obeyed
unique_wizards = {current_wizard}

# Process each duel
for _ in range(N):
    # Read the duel outcome: Z1 defeats Z2
    Z1, Z2 = input().strip().split()

    # If the wand is currently obeying Z2, switch allegiance to Z1
    if current_wizard == Z2:
        current_wizard = Z1
        unique_wizards.add(Z1)  # Add the new wizard to the set of unique wizards

# Output the final wizard the wand is obeying
print(current_wizard)

# Output the number of unique wizards the wand has obeyed
print(len(unique_wizards))

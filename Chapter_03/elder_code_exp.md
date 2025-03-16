To solve this problem in Python, we can follow the steps outlined earlier. Here's the Python code implementation:

```python
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
```

---

### Explanation of the Code:
1. **Input Reading**:
   - The first input is the initial wizard the wand is obeying (`current_wizard`).
   - The second input is the number of duels (`N`).

2. **Tracking Unique Wizards**:
   - A set called `unique_wizards` is used to store all unique wizards the wand has obeyed. It is initialized with the `current_wizard`.

3. **Processing Duels**:
   - For each duel, read the two wizards (`Z1` and `Z2`).
   - If the wand is currently obeying `Z2`, update the `current_wizard` to `Z1` and add `Z1` to the `unique_wizards` set.

4. **Output**:
   - After processing all duels, print the final `current_wizard`.
   - Print the number of unique wizards in the `unique_wizards` set.

---

### Example Input and Output:

#### Input:
```
A
3
B A
C B
A C
```

#### Output:
```
A
3
```

---

### Complexity:
- **Time Complexity**: \(O(N)\), since we process each duel once.
- **Space Complexity**: \(O(1)\), because the set `unique_wizards` can have at most 26 elements (one for each letter of the alphabet).

---

### Edge Cases to Consider:
1. **No Duels**:
   - If `N = 0`, the wand never changes allegiance. The output will be the initial wizard and `1` (since only one wizard has ever obeyed the wand).

2. **All Duels Irrelevant**:
   - If none of the duels involve the current wizard, the wand's allegiance remains unchanged.

3. **Large Input**:
   - The constraints ensure \(N \leq 100\), so the code will run efficiently.

---

This implementation is simple, efficient, and handles all the problem requirements correctly.

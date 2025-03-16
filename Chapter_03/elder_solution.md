This problem simulates a series of duels between wizards, where the Elder Wand changes its allegiance based on the outcomes of these duels. Let's break it down step by step.

---

### Problem Explanation:
1. **Initial State**:
   - The Elder Wand starts by obeying a specific wizard, labeled with an uppercase letter (e.g., `A`).

2. **Duels**:
   - There are `N` duels, where each duel involves two wizards, `Z1` and `Z2`.
   - If `Z1` defeats `Z2`, and the wand is currently obeying `Z2`, then the wand will switch its allegiance to `Z1`.
   - If the wand is not obeying `Z2`, its allegiance remains unchanged.

3. **Questions to Answer**:
   - After all `N` duels, which wizard does the wand obey?
   - How many different wizards did the wand obey during the entire process?

---

### Key Observations:
1. **Wand Allegiance**:
   - The wand's allegiance changes only if the defeated wizard (`Z2`) is the one it is currently obeying.
   - If the wand is obeying `Z2` and `Z1` defeats `Z2`, the wand switches to `Z1`.

2. **Tracking Changes**:
   - You need to keep track of the wand's current allegiance after each duel.
   - You also need to count how many unique wizards the wand obeyed during the process.

---

### Solution Approach:
1. **Initialize**:
   - Start with the initial wizard the wand is obeying.
   - Use a set to keep track of all unique wizards the wand has obeyed.

2. **Process Each Duel**:
   - For each duel, check if the wand is currently obeying the defeated wizard (`Z2`).
   - If yes, update the wand's allegiance to the winner (`Z1`) and add `Z1` to the set of unique wizards.
   - If no, the wand's allegiance remains unchanged.

3. **Output**:
   - After processing all duels, output:
     - The final wizard the wand is obeying.
     - The number of unique wizards in the set.

---

### Example Walkthrough:
Let’s go through an example to understand the process.

#### Input:
```
A
3
B A
C B
A C
```

#### Explanation:
1. **Initial State**:
   - Wand obeys `A`.
   - Set of unique wizards: `{A}`.

2. **First Duel**: `B A`
   - `B` defeats `A`.
   - The wand is currently obeying `A`, so it switches to `B`.
   - Set of unique wizards: `{A, B}`.

3. **Second Duel**: `C B`
   - `C` defeats `B`.
   - The wand is currently obeying `B`, so it switches to `C`.
   - Set of unique wizards: `{A, B, C}`.

4. **Third Duel**: `A C`
   - `A` defeats `C`.
   - The wand is currently obeying `C`, so it switches to `A`.
   - Set of unique wizards: `{A, B, C}`.

#### Output:
```
A
3
```

---

### Complexity:
- Time Complexity: \(O(N)\), since we process each duel once.
- Space Complexity: \(O(1)\), as we only need to store the current allegiance and a set of unique wizards (which has a maximum size of 26).

---

### Final Answer:
For a given sequence of duels, simulate the wand's allegiance changes and track the unique wizards it obeys. Output the final allegiance and the number of unique wizards.

For example:
- Input:
  ```
  A
  3
  B A
  C B
  A C
  ```
- Output:
  ```
  A
  3
  ```

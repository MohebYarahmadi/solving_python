This problem involves a sequence transformation based on specific rules, and you need to determine the number of `A`s and `B`s after a certain number of transformations. Let's break it down step by step.

---

### Problem Explanation:
1. **Initial State**: The machine starts with the letter `A`.
2. **Transformation Rules**:
   - Every `A` in the current word is replaced with `B`.
   - Every `B` in the current word is replaced with `BA`.
3. **Sequence of Transformations**:
   - Start: `A`
   - After 1 press: `B` (A → B)
   - After 2 presses: `BA` (B → BA)
   - After 3 presses: `BAB` (BA → BAB)
   - After 4 presses: `BABBA` (BAB → BABBA)
   - And so on...

The goal is to determine the number of `A`s and `B`s after `K` transformations.

---

### Key Observations:
1. **Pattern Recognition**:
   - The sequence of transformations follows the Fibonacci sequence.
   - Let `A(K)` and `B(K)` represent the number of `A`s and `B`s after `K` transformations.
   - You can observe that:
     - `A(K) = B(K-1)`
     - `B(K) = A(K-1) + B(K-1)`

2. **Base Cases**:
   - For `K = 0`: `A(0) = 1`, `B(0) = 0` (starting with `A`).
   - For `K = 1`: `A(1) = 0`, `B(1) = 1` (after 1 press, `A` becomes `B`).

3. **Recursive Relationship**:
   - The number of `A`s and `B`s at step `K` depends on the counts at step `K-1`.

---

### Solution Approach:
1. **Dynamic Programming**:
   - Use a table or variables to store the counts of `A` and `B` for each step up to `K`.
   - Iterate from `K = 1` to `K = K`, updating the counts based on the rules:
     - `A(K) = B(K-1)`
     - `B(K) = A(K-1) + B(K-1)`

2. **Implementation**:
   - Initialize `A = 1` and `B = 0` for `K = 0`.
   - For each step from `1` to `K`, update:
     - `new_A = B`
     - `new_B = A + B`
     - Update `A = new_A` and `B = new_B`.

3. **Output**:
   - After `K` steps, output the values of `A` and `B`.

---

### Example Walkthrough:
Let’s compute the counts for `K = 4`:
- Start: `A = 1`, `B = 0` (initial state).
- After 1 press: `A = 0`, `B = 1` (A → B).
- After 2 presses: `A = 1`, `B = 1` (B → BA).
- After 3 presses: `A = 1`, `B = 2` (BA → BAB).
- After 4 presses: `A = 2`, `B = 3` (BAB → BABBA).

So, for `K = 4`, the output is `2 3`.

---

### Complexity:
- Time Complexity: \(O(K)\), since we iterate `K` times.
- Space Complexity: \(O(1)\), as we only need to store the counts for the current and previous steps.

---

### Final Answer:
For a given `K`, compute the number of `A`s and `B`s using the dynamic programming approach described above. The output will be the values of `A` and `B` after `K` transformations.

For example:
- Input: `K = 4`
- Output: `2 3`

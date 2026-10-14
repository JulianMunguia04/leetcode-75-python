# 🧩 Two Pointers

This folder contains my Python solutions for problems under the **Two Pointers** section of the [LeetCode 75](https://leetcode.com/studyplan/leetcode-75/).

---

## 📘 Concepts Covered

- Two Pointers

---

## 📋 Prerequisites

- Dynamic Arrays
- Loops
- Two Pointers
- ...

## 🧠 Problems Solved

| # | Problem | Difficulty | File | Topics | Status |
|---|----------|-------------|------|---------|--------|
| 1 | Move Zeroes | 🟢 Easy | `move_zeroes.py` | Two Pointers | ⏳ |
| 2 | Is Sequence | 🟢 Easy | `is_sequence.py` | Two Pointers | ⏳ |
| 3 | Container with Most Water | 🟡 Medium | `container_with_most_water.py` | Two Pointers | ⏳ |
| 4 | Max Numbers K Sum | 🟡 Medium | `max_numbers_k_sum.py` | Two Pointers | ⏳ |

🟢 = Easy 🟡 = Medium 🔴 = Hard  
✅ = Completed 🔄 = In Progress ⏳ = To Do

---

## 📝 Notes

#### Two Pointers
The Two Pointer Technique is an algorithmic pattern where two variables (pointers/indexes) traverse a data structure (usually an array or string) instead of using nested loops.

Instead of a nested loop which is O(n^2) we can do two pointers as follows for O(n):

```python
left = 0
right = len(nums) - 1

while left < right
    ...
```

##### 4 Main Patterns
Opposite Directions (Converging)
- Pointers start at opposite extremes and move toward each other until they meet.
- **Signals:** The input is sorted, you need to find pairs, or the problem involves symmetry
- **Classic Problems:** Two Sum II (Sorted Input), Valid Palindrome, Container With Most Water.

```python
def opposite_direction(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Move rightward to increase the sum
        else:
            right -= 1 # Move leftward to decrease the sum
```

Fast and Slow (The "Tortoise and Hare")


Read / Write (In-Place Modification)

Two Arrays / Iterators (Parallel)

---

## ⚙️ How to Run

Run any problem file directly using Python:

```bash
python3 move_zeroes.py
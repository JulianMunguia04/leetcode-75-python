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
- **Concept:** Pointers start at opposite extremes and move toward each other until they meet.
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
- **Concept:** Pointers start at opposite extremes of a linear collection and move inward toward each other until they meet.
- **Signals:** The input array is sorted, you need to find pairs/triplets matching a constraint, or the problem involves checking for symmetry (like a palindrome).
- **Classic Problems:** Two Sum II (Sorted), Valid Palindrome, 3Sum, Container With Most Water, Reverse String.

```python
def opposite_direction(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Move rightward to increase the sum
        else:
            right -= 1 # Move leftward to decrease the sum
    return []
```

Read / Write (In-Place Modification)
- **Concept:**** Both pointers start at the beginning of the same data structure and move in the same direction. One pointer expands the boundary while the other drags behind to compress it or mark an write-boundary.
- **Signals:** The problem asks to evaluate a continuous subarray or substring matching a criteria, or requires modifying an array in-place to track unique values.
- **Classic Problems:** Longest Substring Without Repeating Characters, Minimum Size Subarray Sum, Remove Duplicates from Sorted Array, Move Zeroes.

```python
def same_direction(nums):
    if not nums:
        return 0
    slow = 0  # Tracks the boundary of valid elements
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]  # Overwrite in-place
    return slow + 1
```

Two Arrays / Iterators (Parallel)
- **Concept:** One pointer is assigned to the first array, and a completely separate pointer is assigned to the second array. They move independently based on comparisons between the two current items.
- **Signals:** You are given two separate sorted lists/arrays and need to combine them, intersect them, or find relative differences between them efficiently.
- **Classic** Problems: Merge Sorted Array, Intersection of Two Arrays, Minimum Common Value, Backspace String Compare.

```python
def two_arrays(arr1, arr2):
    p1, p2 = 0, 0
    merged = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] <= arr2[p2]:
            merged.append(arr1[p1])
            p1 += 1
        else:
            merged.append(arr2[p2])
            p2 += 1
    # Append remaining chunks
    merged.extend(arr1[p1:])
    merged.extend(arr2[p2:])
    return merged
```

---

## ⚙️ How to Run

Run any problem file directly using Python:

```bash
python3 move_zeroes.py
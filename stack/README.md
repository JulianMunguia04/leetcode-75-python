# 🧩 Stack

This folder contains my Python solutions for problems under the **stack** section of the [LeetCode 75](https://leetcode.com/studyplan/leetcode-75/).

---

## 📘 Concepts Covered

- Stack

---

## 📋 Prerequisites

- Dynamic Arrays
- Loops
- Stack
- Strings
- ...

## 🧠 Problems Solved

| # | Problem | Difficulty | File | Topics | Status |
|---|----------|-------------|------|---------|--------|
| 1 | Removing Stars From a String | 🟡 Medium | `removing_stars_from_a_string.py` | Stack | ✅ |

🟢 = Easy 🟡 = Medium 🔴 = Hard  
✅ = Completed 🔄 = In Progress ⏳ = To Do

---

## 📝 Notes

#### Stack
##### Last In, First Out
- Last element added is the first removed
- Use to keep track of **unfinished work**.
- Scan left -> right, storing items until they can be resolved.

##### Python Stack
```python
stack = []

# Push
stack.append(x)

# Pop
stack.pop()

# Peek (top)
stack[-1]

# Empty
if stack:
```

All time complexity O(n)

---

## ⚙️ How to Run

Run any problem file directly using Python:

```bash
python3 removing_stars_from_a_string.py
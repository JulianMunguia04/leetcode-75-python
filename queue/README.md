# 🧩 Queue

This folder contains my Python solutions for problems under the **Queue** section of the [LeetCode 75](https://leetcode.com/studyplan/leetcode-75/).

---

## 📘 Concepts Covered

- Queue

---

## 📋 Prerequisites

- Arrays
- ...

## 🧠 Problems Solved

| # | Problem | Difficulty | File | Topics | Status |
|---|----------|-------------|------|---------|--------|
| 1 | Number of Recent Calls | 🟢 Easy | `number_of_recent_calls.py` | Hashmap | ✅ |

🟢 = Easy 🟡 = Medium 🔴 = Hard  
✅ = Completed 🔄 = In Progress ⏳ = To Do

---

## 📝 Notes

### Queue
Queues are one of the simplest data structures:

FIFO (First in, First Out)
- First person to get in line -> First person served
- New people always join from the back

#### Operations
- Enqueue, add to back, O(1)
- Dequeue, remove from front, O(1)
- Peek, look at front, O(1)
- Empty, Check if queue is empty, O(1)
Can't use a python list becauase dequeue would be a O(n) operation

#### Python Implemenation
Use `collections.deque`
```python
from collections import deque

queue = deque()
```

#### Python Operations
```python
# Enqueue(add)
queue.append(5)
queue.append(10)
print(queue) # deque([5,10])

# Dequeue
front = queue.popleft()

print(front) # 5

# Peek
front = queue[0]

# Empty
if not queue: 
  print("Empty")
```
#### Visualization
```
[3][5][8][10]
 ^
 remove here

append(12)

[3][5][8][10][12]

popleft()

[5][8][10][12]

```

---

## ⚙️ How to Run

Run any problem file directly using Python:

```bash
python3 number_of_recent_calls.py
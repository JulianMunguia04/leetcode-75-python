# 🧩 Linked List

This folder contains my python leetcode solutions for select problems for the topic **linked-list**

---

## 📘 Concepts Covered

- Arrays
- Linked Lists

---

## 📋 Prerequisites

- Dynamic Arrays
- ...

## 🧠 Problems Solved

| # | Problem | Difficulty | File | Topics | Status |
|---|----------|-------------|------|---------|--------|
| 1 | Reverse Linked List | 🟢 Easy | `reverse_linked_list.py` | Linked List | ✅ |
| 2 | Middle of the Linked List | 🟢 Easy | `middle_of_the_linked_list.py` | Linked List | ⏳ |
| 3 | Linked List Cycle II | 🟡 Medium | `linked_list_cycle_2.py` | Linked List | ⏳ |
| 4 | Remove Nth Node From End of List | 🟡 Medium | `remove_nth_node_from_end_of_list.py` | Linked List | ⏳ |
| 5 | LRU Cache | 🟡 Medium | `lru_cache.py` | Linked List | ⏳ |
| 6 | Merge k Sorted Lists | 🔴 Hard | `merge_k_sorted_lists.py` | Linked List | ⏳ |


🟢 = Easy 🟡 = Medium 🔴 = Hard  
✅ = Completed 🔄 = In Progress ⏳ = To Do

---

## 📝 Notes

### Linked Lists
A linked list is a chain of objects called **nodes**
``` 
10 → 20 → 30 → None 
```

Each node contains:
- Value
- Next

For example
```
Node(10)
   |
   v
Node(20)
   |
   v
Node(30)
   |
   v
  None
```
#### Python Linked Lists
The node class in Python
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Create a Node
node1 = ListNode(10)

#Create another node link
node2 = ListNode(20)
node1.next = node2
```

This will create
```
node1
  |
  v
┌──────────────┐
│ val = 10     │
│ next ────────┼─────┐
└──────────────┘     |
                     v
                ┌──────────────┐
                │ val = 20     │
                │ next = None  │
                └──────────────┘
```
##### What is Head?
We don't keep track of every node
Only the first node which we call `head`
```
head
 |
 v
10 → 20 → 30 → None
```
In Python 
```python
head = ListNode(10)

head.next = ListNode(20)
head.next.next = ListNode(30)
```

##### Local Setup
Either using the Python Class manually or by importiung the ListNode class
```python
from linked_list import ListNode


head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)


current = head

while current:
    print(current.val)
    current = current.next
```
---

## ⚙️ How to Run

Run any problem file directly using Python:

```bash
python3 reverse_linked_list.py

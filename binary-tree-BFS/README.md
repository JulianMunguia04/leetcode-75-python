# 🧩 Binary Tree - BFS

This folder contains my Python solutions for problems under the **Binary Tree - BFS** section of the [LeetCode 75](https://leetcode.com/studyplan/leetcode-75/).

---

## 📘 Concepts Covered

- Binary Tree
- Pointers

---

## 📋 Prerequisites

- Pointers
- Linked List

## 🧠 Problems Solved

| # | Problem | Difficulty | File | Topics | Status |
|---|----------|-------------|------|---------|--------|
| 1 | Binary Tree Right Side View | 🟢 Easy | `binary_tree_right_side_view.py` | BT DFS | ✅ |
| 2 | Leaf-Similar Trees | 🟢 Easy | `maximum_level_sum_binary_tree.py` | BT DFS | ⏳ |


🟢 = Easy 🟡 = Medium 🔴 = Hard  
✅ = Completed 🔄 = In Progress ⏳ = To Do 

---

## 📝 Notes

### Binary Tree
Binary tree is a collection of nodes where every node can have:
- a `val`
- a `left` child
- a `right` child

For example:
```
        1
       / \
      2   3
     / \
    4   5
```
In python, LeetCode usually gives this:
```Python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

#### Binary Tree - BFS
Breadth First Search

---

## ⚙️ How to Run

Run any problem file directly using Python:

```bash
python3 binary_tree_right_side_view.py
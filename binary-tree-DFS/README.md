# 🧩 Binary Tree - DFS

This folder contains my Python solutions for problems under the **Binary Tree - DFS** section of the [LeetCode 75](https://leetcode.com/studyplan/leetcode-75/).

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
| 1 | Maximum Depth of Binary Tree | 🟢 Easy | `maximum_depth_of_binary_tree.py` | BT DFS | ⏳ |
| 2 | Leaf-Similar Trees | 🟢 Easy | `leaf_similar_trees.py` | BT DFS | ⏳ |
| 3 | Count Good Nodes in Binary Tree | 🟡 Medium | `count_good_nodes_in_a_binary_tree.py` | BT DFS | ⏳ |
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
In python, LeetCode usually gives you this:
```Python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

#### Binary Tree - DFS

---

## ⚙️ How to Run

Run any problem file directly using Python:

```bash
python3 maximum_depth_of_binary_tree.py
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
In python, LeetCode usually gives this:
```Python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

#### Binary Tree - DFS
Depth first search

Pick a node → go as deep as possible → come back → explore the other side.

For:
```
        1
       / \
      2   3
     / \
    4   5
```
DFS might travel:
```
1 → 2 → 4
        ↑
        back
      → 5
        ↑
        back
1 → 3
```
DFS naturally fits recursion

##### Most Important DFS Pattern
```
def dfs(node):

    if node is None:
        return

    # do something with node

    dfs(node.left)
    dfs(node.right)
```

### Setup
Tree Node
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Manually Creating a Tree
- Example
```
        1
       / \
      2   3
     / \
    4   5
```
In python:
```python
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
```

View Tree
```python
print(root.val)

print(root.left.val)
print(root.right.val)

print(root.left.left.val)
print(root.left.right.val)
```

#### DFS Basic Setup
```python
def dfs(node):

    if node is None:
        return

    print(node.val)

    dfs(node.left)
    dfs(node.right)
```

---

## ⚙️ How to Run

Run any problem file directly using Python:

```bash
python3 maximum_depth_of_binary_tree.py
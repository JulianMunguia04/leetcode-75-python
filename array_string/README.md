# 🧩 Arrays / String

This folder contains my Python solutions for problems under the **Arrays / Hashing** section of the [LeetCode 75](https://leetcode.com/studyplan/leetcode-75/).

---

## 📘 Concepts Covered

- Arrays
- Strings

---

## 📋 Prerequisites

- Dynamic Arrays
- ...

## 🧠 Problems Solved

| # | Problem | Difficulty | File | Topics | Status |
|---|----------|-------------|------|---------|--------|
| 1 | Merge Strings Alternately | 🟢 Easy | `greatest_common_divisor_of_strings.py` | String | ⏳ |
| 2 | Greatest Common Divisor if Strings | 🟢 Easy | `greatest_common_divisor_of_strings.py` | String | ⏳ |
| 3 | Kids With the Greatest Number of Candies | 🟢 Easy | `kids_with_the_greatest_number_of_candies.py` | String | ⏳ |
| 4 | Can Place Flowers | 🟢 Easy | `can_place_flowewrs.py` | String | ⏳ |
| 5 | Reverse Vowels of a String | 🟢 Easy | `reverse_vowels_of_a_string.py` | String | ⏳ |
| 6 | Reverse Words of a String | 🟡 Medium | `reverse_words_of_a_string.py` | String | ⏳ |
| 7 | Product of Array Except Self | 🟡 Medium | `product_of_array_except_self.py` | String | ⏳ |
| 8 | Increasing Triplet Subsequence | 🟡 Medium | `increasing_triplet_subsequence.py` | String | ⏳ |
| 9 | String Compression | 🟡 Medium | `string_compression.py` | String | ⏳ |

🟢 = Easy 🟡 = Medium 🔴 = Hard  
✅ = Completed 🔄 = In Progress ⏳ = To Do

---

## 📝 Notes

#### Python Lists
Python lists are dynamic arrays that automatically resize
```python
nums = []
nums.append(1)
nums.append(2)
nums.append(3)
```
Memory grows automatically.

#### Arrays
An ordered collection of elements, in python this usually refers to a **list**

```python
nums = [1,2,3,4,5]
```

A python list is basically a dynamic array
Python arrays support indexing which is a O(1)(Constant Time) to access any element we have the index for.

```python
nums[0]     # The first element
nums[2]     # The third element
nums[-1]    # The last element
```

##### Array Operations
Access an element by index, Time: O(1)
```python
nums[i]
```

Change an element, Time O(1)
```python
nums[1] = 10
```

Add to the end, Time: O(1) if there is space allocated, if not it is O(n) because it needs to be rewriten completely
```python
nums.append(10)
```

Remove from the end, Time: O(1)
```python
nums.pop()

# Can also return this value
x = nums.pop()

# And use index to pop
nums.pop(1) removes element at index 1
# This is O(n) linear time
```

Insert, usually O(n) becuase elements need to shift
```python
nums.insert(i, x)
```

Remove by value, Time: O(n)
```python
nums.remove(5)
```

Check whether something exists, O(n)
```python
if 5 in nums:
    ...
```
Better to use a set

#### Strings
A string is a linear data structure that represents a sequential collection of characters. Unlike **primitive** data types like intergers or booleans that store a single value, a string acts as a container for storing and manipulating textual information.

Strings are immutable sequences of characters

---

## ⚙️ How to Run

Run any problem file directly using Python:

```bash
python3 greatest_common_divisor_of_strings.py
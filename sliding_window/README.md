# 🧩 Sliding Window

This folder contains my Python solutions for problems under the **Sliding Window** section of the [LeetCode 75](https://leetcode.com/studyplan/leetcode-75/).

---

## 📘 Concepts Covered

- Sliding Window

---

## 📋 Prerequisites

- Sliding Window
- ...

## 🧠 Problems Solved

| # | Problem | Difficulty | File | Topics | Status |
|---|----------|-------------|------|---------|--------|
| 1 | Maximum Average Subarray I | 🟢 Easy | `maximum_average_subarray_one.py` | Sliding Window | ⏳ |
| 2 | Maximum Number of Vowels in a Substring of Given Length | 🟡 Medium | `max_num_of_vowels_in_a_substring_given_length.py` | Sliding Window | ⏳ |
| 3 | Max Consecutive Ones III | 🟡 Medium | `max_consecutive_ones_3.py` | Sliding Window | ⏳ |
| 4 | Longest Subarray of 1's After Deleting One Element | 🟡 Medium | `longest_subarray_of_1s_after_deleting_one_element.py` | Sliding Window | ⏳ |

🟢 = Easy 🟡 = Medium 🔴 = Hard  
✅ = Completed 🔄 = In Progress ⏳ = To Do

---

## 📝 Notes

#### Sliding Window
A sliding window is a technique that processes contiguous subarrays or substrings without recalculating everything each time.

Instead of checking every possible window from scratch (O(n²)), we:
- expand the window
- shrink the window when needed
- update our answer as we move

Result:

- O(n) instead of O(n²)

##### When to use sliding window
Find questions like
- contiguous
- consecutive
- substring
- subarray
- longest
- shortest
- maximum
- minimum
- at most
- at least
- exactly K
- window
- continuous sequence

##### Two Major Implementations
**Fixed-Size Sliding Window**
- Used when the problem explicitely specifies the length of the window.
- Grow the window to size K, then slide it forward by adding one element to the right and subtracting one from the left

```python 
def fixed_sliding_window(arr, k):
    # 1. Initialize the running state for the first window
    current_window_state = sum(arr[:k])  # Example state: a sum
    max_state = current_window_state
    
    # 2. Slide the window from index k to the end of the array
    for r in range(k, len(arr)):
        # Add the incoming element (right pointer)
        current_window_state += arr[r]
        # Remove the outgoing element (left pointer, which is r - k)
        current_window_state -= arr[r - k]
        
        # 3. Update your result
        max_state = max(max_state, current_window_state)
        
    return max_state
```

**Variable-Size Sliding Window**
- Used when the window size depends on a specific constraint (e.g., "find the longest subarray wiht at most 2 distinct chars")
- Use two pointers, `l` (left) and `r` (right). Expand `r` to explore. The momenet the window becomes invalid (violates the constraint), shrink `l` until it becomes valid again.

```python
def variable_sliding_window(arr):
    l = 0
    max_len = 0
    window_state = {} # Often a hash map or set to track frequencies/elements

    for r in range(len(arr)):
        # 1. Add the right element to the current state
        window_state[arr[r]] = window_state.get(arr[r], 0) + 1
        
        # 2. Shrink the window from the left while the condition is violated
        while condition_violated(window_state):
            window_state[arr[l]] -= 1
            if window_state[arr[l]] == 0:
                del window_state[arr[l]]
            l += 1 # Shrink window
            
        # 3. Update global maximum (window is valid here)
        max_len = max(max_len, r - l + 1)
        
    return max_len
```

---

## ⚙️ How to Run

Run any problem file directly using Python:

```bash
python3 maximum_average_subarray_one.py
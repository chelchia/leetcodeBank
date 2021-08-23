# Quickselect and Quicksort
### What is quickselect?
Goal: Find the k smallest element in a group, i.e. there are k elements of value <= the target element. 

Intuition: We maintain a pivot p, where elements smaller than or equal to p are moved to its left and elements larger than p 
are moved to its right. Stop when there are k elements to the left of p. This means we have found a p which is the 
kth smallest element.

### Question bank
QS1. [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
- Medium
- Summary: Given an array of points, return k closest points to origin.
- Solution 1: O(n^3) brute force.
- Solution 2: O(nlogk) heap with simple modification to maintain heap of max size k.
- Solution 3: O(n) with quickselect.

[Python](https://github.com/chelchia/leetcodeBank/blob/main/quickselect/qs1.py)

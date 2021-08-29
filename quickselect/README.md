# Quickselect and Quicksort
### What is quickselect?
A smart O(logn) algorithm used to find the kth smallest element in a group, i.e. there are k elements of value <= the target element. 
You can also use this to find the kth largest element with a simple modification.

Intuition: We maintain a pivot p, where elements smaller than or equal to p are moved to its left and elements larger than p 
are moved to its right. Stop when there are k elements to the left of p. This means we have found a p which is the 
kth smallest element.

Implementation: We can implement quickselect in two parts, with the **sort** and **partition** functions.
- Sort: Intuition is a bit like binary search. If there are k elements <= curr pivot, we found the solution. Elif there are fewer than k 
elements <= curr pivot, recurse right (target pivot is on the right). Else recurse left.
- Partition: This is the meat of the solution where we iterate through our current range of elements and arrange them such that the pivot 
is in the middle, with the left half containing elements <= pivot and the right half containing elements > pivot.

### Question bank
QS1. [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
- Medium
- Summary: Given an array of points, return k closest points to origin.
- Solution 1: O(n^3) brute force.
- Solution 2: O(nlogk) heap with simple modification to maintain heap of max size k.
- Solution 3: O(n) with quickselect.

[Python](https://github.com/chelchia/leetcodeBank/blob/main/quickselect/qs1.py)
[C++, using multimap](https://github.com/chelchia/leetcodeBank/blob/main/quickselect/qs1.cpp)

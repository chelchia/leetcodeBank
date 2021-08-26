# Pointer-related approaches
### Two-pointer
Impt: Probably the most common technique tested in interviews, together with DP, search (DFS/BFS) and hash tables.

Good for one-pass solutions to linear DS (array/linked list) questions. The general idea involves keeping track of two "pointers", 
most often to bound the start and end of a range (as in sliding window). Another common intuition is to use one pointer as the 
"adventurous" pointer, which searches for the next target element, and the other pointer as the "memory" pointer, which keeps track 
of some important index which has been traversed before (see question P1 for an example).

### Sliding window
Very powerful in certain array/string parsing questions, often linear in time complexity. If the question requires examining a 
"window" of elements at a time, consider using sliding window. Quite commonly used in questions like "Longest substring with XXXX" 
where XXXX is some criteria. See question P5 for example.

### Floyd's algorithm aka the Tortoise and the Hare
Click [here](https://medium.com/@tuvo1106/the-tortoise-and-the-hare-floyds-algorithm-87badf5f7d41) for detailed explanation.

The most common application is linked list cycle detection (see question P4). Imagine a slow and a fast runner. The slow runner 
travels one node per iteration and the fast runner travels two nodes per iteration. They start from the same place. If they meet 
again, there is a cycle in the list. If the fast runner hits a null node (end of list), there is no cycle.

Why does this work? The fast runner increases the distance between himself and the slow runner by one additional node per iteration. 
If there is a cycle, eventually the distance between them will be exactly the length of the (circular) list, which means they are on 
the same node! O(n) time, O(1) space.

### Question bank
P1. In-place removal of duplicates from sorted array
- Easy
- Summary: Given a sorted integer array, remove the duplicates in-place.
- Solution: O(n) one-pass solution using two pointers. As we iterate through the array, place unique elements 
on the left. Since the array is sorted, we don't need a hash table. Use the first pointer to keep track of the 
end of the unique array. The second pointer looks for the next unique element. When found a unique element, swap 
it with the element pointed by the first pointer.

P2. Two Sum
- Easy
- Summary: Given an array of integers, return **indices** of two numbers adding up to a given target.
- Solution 1: O(n) one-pass hash table approach.
- Solution 2: O(nlogn) sorting + 2 pointer approach. After sorting, init left pointer at start of array and right pointer 
at end of array. Increase start if sum < target, or decrease end if sum > target.

P3. Three Sum

P4. [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- Easy
- Summary: Given the head of a linked list, determine if the linked list has a cycle in it.
- Solution 1: O(n) time, O(n) space hash table. Hash the **addresses** of the nodes. If you encounter the same address, there is a cycle.
- Solution 2: O(n) time, in-place Floyd's algorithm for cycle detection.
- Solution 3: O(n) time, in-place but destructive approach. As you traverse the list, change the values to a special character like '#' to mark 
it as visited. If you encounter this special character again, there is a cycle.

P5. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- Medium
- Summary: Given a string, find the length of the longest substring without repeating characters.
- Solution: O(n) sliding window + hash table.

[Python](https://github.com/chelchia/leetcodeBank/blob/main/pointers/p5.py)

P6. [Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- Easy
- Summary: Given an integer array, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
- Solution: One-pass two pointer approach. Your first thought is probably try to bubble the zeroes to the back of the array by swapping them with 
the numbers at the back. But this destroys the order of the non-zero elements. The trick is to approach it by pushing the non-zero elements to the 
front instead. Then the zeroes are naturally bubbled to the back. Whenever you encounter a non-zero element, swap it towards the left.

The intermediate array will look something like this: 7913**0**000**1**283010042. Left and right pointers highlighted. In this round, we swap 1 with the 
0 pointed by the left pointer.

# Sorting
Instead of discussing specific sorting algorithms, this section focuses on how sorting (could be calling standard lib sort) 
can help you solve certain problems.

### Question Bank
S1. Valid anagram
- Summary: Given two strings, determine if they are anagrams. E.g. listen and silent are anagrams.
- Solution 1: O(nlogn) sort both strings. If result is identical, they are anagrams.
- Solution 2: O(n) hash table. Count occurrences of each letter for both strings and compare the tables.

Extension: Group anagrams
- Summary: Given an array of strings, group the anagrams together.
- Solution: Use sorted strings as keys for a hash table. Append anagrams (unsorted) in a list for each key.

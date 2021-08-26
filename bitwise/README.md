# Bitwise operations
### Important rules to note
**a^a = 0**							, where ^ represents XOR

### Question bank
BW1. Single number
- Easy if you know the solution :D
- Summary: In an array of integers, every element appears twice except for one. Find that one.
- Solution: XOR every item in the array. We will be left with the unique number b according to the 
formula **a^b^a = (a^a)^b = 0^b = b**.
- Pseudocode:

        a = 0
        For every num in arr:
            a ^= num
        return a

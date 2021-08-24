class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep a sliding window with start ptr and end ptr
        # use a dictionary key=char in curr substr and val=idx of the char in the string
        # whenever we encounter a repeat char, modify start to become idx+1 of the existing char, and
        # store the pos of the newly encountered char
        # we can do this in one pass -- O(n)
        ch_pos = dict()
        start=end=0
        max_so_far=0
        
        for i in range(len(s)):
            ch = s[i]
            if ch not in ch_pos or ch not in s[start:end+1]:
                ch_pos[ch] = i
            else:
                idx = ch_pos[ch]
                start = idx+1
                ch_pos[ch] = i
            end = i
            max_so_far = max(max_so_far, end - start + 1)
        return max_so_far

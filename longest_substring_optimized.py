class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Use of dictionary
        used = {}
        max_length = start = 0
        # here, i will represent the index of string
        # and c will represent value of string 
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1 
            else:
                max_length = max(max_length, i - start + 1)
                
            used[c] = i
            
        return max_length

s= Solution()
print(s.lengthOfLongestSubstring('aggdfsggshhd***8745214#@$^%'))  
      
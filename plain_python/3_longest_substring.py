# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        def consume_one(work_str: str, cur: str) -> (str, str):
            if len(work_str)>0:
                cur_char = work_str[0]
                if cur_char in cur:
                    return (cur, work_str)
                else:
                    cur += cur_char
                    work_str = work_str[1:]
                    return consume_one(work_str, cur)
            else:
                return (cur, work_str)
        
        def get_longest_substr(work_str: str, cur_longest: str) -> str:
            next_substr, work_str = consume_one(work_str, "")
            if len(next_substr) > len(cur_longest):
                cur_longest = next_substr
            if len(work_str)==0:
                return cur_longest
            else:
                return get_longest_substr(work_str, cur_longest)
        
        return len(get_longest_substr(s, ""))
    
if __name__=='__main__':
    s="abcabcbb"
    print(Solution.lengthOfLongestSubstring(s))
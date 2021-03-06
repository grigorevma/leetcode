'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
 No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

'''
class Solution:
    # Runtime 72ms 20%
    # Memory 12.8mb 100%
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)==0 or len(t)==0:
            return True
        new_dict , new_dict2 =  {}, {}
        new_string, new_string2 = "", ""
        count = 0
        value, value2 = s[0], t[0]
        for i in range(len(s)):
            new_dict.setdefault(s[i], count)
            new_dict2.setdefault(t[i], count)
            count += 1
            new_string += str(new_dict[s[i]])
            new_string2 += str(new_dict2[t[i]])
            value, value2 = s[i], t[i]
        return new_string == new_string2
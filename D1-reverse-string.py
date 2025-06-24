"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Leetcode - https://leetcode.com/problems/reverse-string/
"""

# Approach used 2 pointer
"""
We use 2 pointers one form the starting and second from the end and
then we are replacing both with each other 
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
       
        # Initialize two pointers left and right for both the ends

        left, right = 0, len(s)-1
        
        # A while loop which will run till both the pointers meet in the middle
        while left < right:
            
            # Swapping with each other
            s[left], s[right] = s[right], s[left]

	    # Increment the left pointer by 1
            left +=1

	    # decrement the right pointer by 1
            right -=1

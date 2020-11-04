Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store 
integers within the 32-bit signed integer 
range: [−231,  231 − 1]. For the purpose 
of this problem, assume that your function returns 0 when 
the reversed integer overflows.

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0

def reverse(self, x: int) -> int:
    s = -1 if x < 0 else 1
    x_ = str(x)[-1::-1] if s == 1 else str(x) [-1:0:-1]
    ans = s*int(x_)
    return ans if abs(ans) < 2**31 else 0

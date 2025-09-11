# Last updated: 9/11/2025, 12:31:11 PM
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [] # hold ints where to stop/start
        ans = [] # hold the chars
        stack_index = 0 # curr index in ans array
        for i in range(len(s)): # i keep tracks of prenthese index too
            if s[i] == "(":
                stack.append(stack_index)

            elif s[i] == ")":
                r = stack.pop() # can't pop it twice so u do it once
                ans[r:stack_index+1] = ans[r:stack_index+1][::-1] # setting the splice equal to the splice reversed .reversed() doesn't exist
            else: # it's a letter
                ans.append(s[i])
                stack_index += 1
        return "".join(ans)
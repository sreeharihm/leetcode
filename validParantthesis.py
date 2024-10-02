class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            else:
                if not stack or (s[i]==')' and stack[-1]!='(') or (s[i]==']' and stack[-1]!='[') or (s[i]=='}' and stack[-1]!='{'):
                    return False
                stack.pop()        
        return not stack
            
a = Solution()
print(a.isValid("((([)]))")) 
'''Time complexity- O(n)-length of string
    Space complexity - O(n)
'''
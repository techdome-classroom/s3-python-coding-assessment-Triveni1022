class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        
        stack = []
        return self.valid(s, stack)
    
    def valid(self, s, stack):
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    return False
                top_char = stack.pop()
                if (char == ')' and top_char != '(') or \
                   (char == ']' and top_char != '[') or \
                   (char == '}' and top_char != '{'):
                    return False
        return not stack

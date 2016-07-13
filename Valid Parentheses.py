dict = {}
dict['('] = ')'
dict['['] = ']'
dict['{'] = '}'
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for ch in s:
            if dict.get(ch) != None:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if dict.get(top) == None:
                    return False
                if dict[top] != ch:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False
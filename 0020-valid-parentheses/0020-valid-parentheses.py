class Solution(object):
    def isValid(self, s):
        stack = []

        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != mapping[char]:
                    return False

        return len(stack) == 0
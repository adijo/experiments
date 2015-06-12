
class Solution:
    def peek(self, stack):
        return stack[len(stack) - 1]

    def tokenize(self, s):
        l = []
        last = []
        for char in s:
            if char == '+' or char == '-' or char == ')':
                if len(last) > 0: 
                    l.append(''.join(last))
                l.append(char)
                last = []
            elif char == '(' or char == ')':
                l.append(char)
            elif char != ' ':
                last.append(char)
        if len(last) > 0 and last[0] != ' ': 
            l.append(''.join(last))
        return l

    def postfix(self, arr):
        stack = []
        buffer = []
        for char in arr:
            if char == '+' or char == '-':
                if len(stack) > 0 and self.peek(stack) == '(':
                    stack.append(char)
                else:
                    if len(stack) > 0:
                        buffer.append(stack.pop())
                    stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                flag = True
                while flag:
                    popped = stack.pop()
                    if popped == '(':
                        flag = False
                    else:
                        buffer.append(popped)
            else:
                buffer.append(char)
        while len(stack) > 0:
            buffer.append(stack.pop())
        return buffer


    def evaluate(self, postfix):
        stack = []
        for char in postfix:
            if char == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif char == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            else:
                stack.append(char)
        assert len(stack) == 1
        return stack[0]

    def calculate(self, s):
        arr = self.tokenize(s)
        __postfix = self.postfix(arr)
        answer = self.evaluate(__postfix)
        return int(answer)

s = Solution()
print s.calculate("(3 + 2) - 1")


class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        ops = ['+','-','*','/']
        for token in A:
            if token not in ops:
                stack.append(token)
            else:
                second_operand = str(stack.pop())
                first_operand = str(stack.pop())
                val = int(eval(first_operand+token+second_operand))
                stack.append(val)
        return stack.pop()
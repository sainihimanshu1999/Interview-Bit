class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = []
        max_area = 0
        index = 0
        while index<len(A):
            if(not stack) or(A[stack[-1]] <= A[index]):
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                
                
                area = (A[top_of_stack]*((index - stack[-1]-1) if stack else index))
                
                max_area = max(max_area,area)
        while stack:
            top_of_stack = stack.pop()
            
            area = (A[top_of_stack]*((index - stack[-1]-1) if stack else index))
                
            max_area = max(max_area,area)
        
        return max_area
            

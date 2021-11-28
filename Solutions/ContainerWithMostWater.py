Optimized Solution:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
             return height[1] if height[1] < height[0] else height[0]
        left = 0
        right = len(height) - 1
        max_product = 1
        while left < right:
            max_product = max(max_product, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_product
        
Naive Solution:
class Solution:
    def maxArea(self, height: List[int]) -> int:      
         if len(height) == 2:
             return height[1] if height[1] < height[0] else height[0]
         length, breadth = 0, 0
         current_product = -1
         global_product = -1
         j = len(height) - 1
         i = len(height) - 2
         while j >= 1:
             if height[j] > height[i]:
                 breadth = height[i]
             else:
                 breadth = height[j]
             length = j - i
             current_product = max(current_product, length*breadth)
             if current_product > global_product: 
                 global_product = current_product
             if i == 0:
                 j -= 1
                 i = j - 1
             else:
                 i -= 1
         return global_product

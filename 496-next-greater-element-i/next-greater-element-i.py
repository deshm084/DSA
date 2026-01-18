class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)
        while stack:
            next_greater[stack.pop()] = -1
        result = []
        for num in nums1:
            result.append(next_greater[num])
        return result

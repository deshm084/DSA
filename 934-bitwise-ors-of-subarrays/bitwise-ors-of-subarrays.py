class Solution:
    def subarrayBitwiseORs(self, nums: List[int]) -> int:
        result = set()
        prev = set()
        for num in nums:
            curr = set()
            for val in prev:
                curr.add(val | num)
            curr.add(num)
            result.update(curr)
            prev = curr
        return len(result)
        
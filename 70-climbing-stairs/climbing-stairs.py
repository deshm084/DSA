class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        ways_one_step_before = 2
        ways_two_steps_before = 1
        for step in range(3, n + 1 ):
            current_ways = ways_one_step_before + ways_two_steps_before
            ways_two_steps_before = ways_one_step_before
            ways_one_step_before =current_ways
        return ways_one_step_before
        
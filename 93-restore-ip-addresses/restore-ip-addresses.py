class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        parts = []
        def backtrack(index):
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return
            for length in range(1, 4):
                if index + length > len(s):
                    break
                part  = s[index:index + length] 
                if part[0] == '0' and length > 1:
                    continue
                if int(part) > 255:
                    continue
                parts.append(part)
                backtrack(index + length)
                parts.pop()
        backtrack(0)
        return result
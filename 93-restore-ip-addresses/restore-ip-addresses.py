class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def backtrack(index, parts, current_ip):
            if parts == 4 and index == len(s):
                result.append(".".join(current_ip))
                return
            if parts == 4 or index == len(s):
                return 
            for length in range (1, 4):
                if index + length > len(s):
                    break
                part = s[index:index + length]
                if part.startswith('0') and len(part) > 1:
                    continue
                if int(part) <= 255:
                    current_ip.append(part)
                    backtrack(index + length, parts + 1, current_ip)
                    current_ip.pop()
        backtrack(0, 0, [])
        return result



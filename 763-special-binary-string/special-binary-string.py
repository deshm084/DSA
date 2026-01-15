class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        special_substrings = []
        balance = 0
        start = 0
        for i in range(len(s)):
            if s[i] == '1':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                inner = self.makeLargestSpecial(s[start + 1:i])
                special_substrings.append( '1' + inner + '0')
                start = i + 1
        special_substrings.sort(reverse = True)
        return ''.join(special_substrings)
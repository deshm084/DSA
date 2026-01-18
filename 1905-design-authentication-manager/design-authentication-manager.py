from collections import deque

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}                 # tokenId -> expiry time
        self.queue = deque()             # (expiryTime, tokenId)

    def _remove_expired(self, currentTime: int):
        # remove all expired tokens
        while self.queue and self.queue[0][0] <= currentTime:
            expiry, tokenId = self.queue.popleft()
            # only delete if this expiry is still the active one
            if self.tokens.get(tokenId) == expiry:
                del self.tokens[tokenId]

    def generate(self, tokenId: str, currentTime: int) -> None:
        self._remove_expired(currentTime)
        expiryTime = currentTime + self.timeToLive
        self.tokens[tokenId] = expiryTime
        self.queue.append((expiryTime, tokenId))

    def renew(self, tokenId: str, currentTime: int) -> None:
        self._remove_expired(currentTime)
        if tokenId in self.tokens:
            newExpiry = currentTime + self.timeToLive
            self.tokens[tokenId] = newExpiry
            self.queue.append((newExpiry, tokenId))

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._remove_expired(currentTime)
        return len(self.tokens)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
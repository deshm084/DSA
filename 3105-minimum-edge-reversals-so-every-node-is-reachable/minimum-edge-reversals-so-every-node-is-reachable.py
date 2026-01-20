class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        # build graph with cost
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append((v, 0))  # correct direction
            graph[v].append((u, 1))  # needs reversal
        
        answer = [0] * n
        
        # first DFS to compute reversals needed when root is 0
        def dfs1(node, parent):
            total = 0
            for nei, cost in graph[node]:
                if nei != parent:
                    total += cost + dfs1(nei, node)
            return total
        
        answer[0] = dfs1(0, -1)
        
        # second DFS to reroot and compute answers
        def dfs2(node, parent):
            for nei, cost in graph[node]:
                if nei != parent:
                    if cost == 0:
                        answer[nei] = answer[node] + 1
                    else:
                        answer[nei] = answer[node] - 1
                    dfs2(nei, node)
        
        dfs2(0, -1)
        return answer
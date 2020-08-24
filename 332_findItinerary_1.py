from typing import List
import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Eulerian path
        graph = collections.defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
        for tos in graph.values():
            tos.sort(reverse=True)
        res = []
        self.dfs(graph, 'JKF', res)
    
    def dfs(self, graph, temp, res):
        while graph[temp]:
            v = graph[temp].pop()
            self.dfs(graph, v, res)
        res.append(temp)


if __name__ == "__main__":
    s = Solution()
    s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])\
        == ["JFK", "MUC", "LHR", "SFO", "SJC"]
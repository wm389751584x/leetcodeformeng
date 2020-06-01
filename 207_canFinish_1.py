from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        ranks = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            ranks[u] += 1
        
        queue = []

        # push node with no dependency (rank = 0) to queue
        for i, v in enumerate(ranks):
            if v == 0: queue.append(i)
        
        # bfs kahn algro
        while queue:
            f = queue.pop(0)
            numCourses -= 1
            for r in graph[f]:
                ranks[r] -= 1
                if ranks[r] == 0: queue.append(r)
        return numCourses == 0


if __name__ == "__main__":
    s = Solution()
    assert s.canFinish(4,[[0,1],[0,2],[1,3],[2,3]]) == True





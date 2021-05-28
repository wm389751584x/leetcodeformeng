import collections
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        graph = collections.defaultdict(set)

        for bus, route in enumerate(routes):
            for stop in route: 
                graph[stop].add(bus)

        ans = 0
        visited_stops = set()
        visited_bus = set()
        queue = collections.deque([source])

        visited_stops.add(source)

        while queue:
            for _ in range(len(queue)):
                stop = queue.popleft()

                if stop == target:
                    return ans
                
                for bus in graph[stop]:
                    if bus not in visited_bus:
                        for new_stop in routes[bus]:
                            if new_stop not in visited_stops:
                                queue.append(new_stop)
                                visited_stops.add(new_stop)
            ans += 1
                    
        return -1


if __name__ == "__main__":
    pass
from math import inf
from heapq import heappush, heappop
from collections import deque

graph = [[1],[2,3],[1,4],[4],[3]]

def dijkstra(graph, start, end):
    distabce_to_start = [inf]*len(graph)
    ways_to_get_to = [[] for x in range(len(graph))]
    distabce_to_start[start] = 0
    queue = []
    heappush(queue, start)
    while queue:
        cur = heappop(queue)
        if cur == end:
            break
        for path in graph[cur]:
            ways_to_get_to[path].append(cur)
            if  distabce_to_start[path] > distabce_to_start[cur]+1:
                distabce_to_start[path] = distabce_to_start[cur]+1
                heappush(queue, path)
    result = deque([end])
    while result[0] != start:
        closest_node = None
        closest_distabce = inf
        for path in ways_to_get_to[result[0]]:
            if closest_distabce > distabce_to_start[path]:
                closest_distabce = distabce_to_start[path]
                closest_node = path
        result.appendleft(closest_node)
    return list(result)

print(dijkstra(graph,0,4))
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        for i in range(n):
            if i not in graph:
                graph[i] = []
        
        print(graph)
        
        visited = set()
        connected = 0
        # visited = {0}
        # connected = 0
        # def dfs(node):
        #     for value in graph[node]:

        def dfs(key):
            for value in graph[key]:
                if value not in visited:
                    visited.add(value)
                    dfs(value)

        for i in range(n):
            print(f"outer - {i}")
            if i not in visited:
                print(f"inner - {i}")
                visited.add(i)
                print(visited)
                dfs(i)
                print(visited)
                connected += 1


        return connected


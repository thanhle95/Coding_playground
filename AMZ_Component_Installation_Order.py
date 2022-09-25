# To assemble an Amazon robot, we are given N components labeled from 0 ~ N-1.
# There are order requirements to put some components given by an array of pair [pre, post]
# which means pre must be installed before post. Write a solution to determine if all the components
# can be assmbled successfully.
# ex [[0,1],[1,2],[2,0]] returns false


# Solution same with Course Schedule

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        
        # build graph
        for pair in prerequisites:
            c, pre = pair
            graph[c].append(pre)
            
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
            
        return True
    
    def dfs(self, graph, visited, i):
        if visited[i] == -1:
            return False
        
        if visited[i] == 1:
            return True
        
        visited[i] = -1
        
        for node in graph[i]:
            if not self.dfs(graph, visited, node):
                return False
        
        visited[i] = 1
        return True


print(Solution().canFinish(3, [[0,1],[1,2],[2,0]]))
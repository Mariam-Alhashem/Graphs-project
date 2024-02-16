#hi

# a helper method for is fully connected method 
def dfs(self, node, visited):
       if node not in visited:
           visited.add(node)
           for neighbor in self.graph[node]:
               self.dfs(neighbor, visited)

#here should be the class
class NetworkGraph:
   def __init__(self):
       self.graph = {}  # adjacency list representation
   def add_computer(self, computer):
       if computer not in self.graph:
           self.graph[computer] = []
       # a helper method for is fully connected method 
   def dfs(self, node, visited):
       if node not in visited:
            visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs(neighbor, visited)
   def add_connection(self, computer1, computer2):
       if computer1 in self.graph and computer2 in self.graph:
             self.graph[computer1].append(computer2)
             self.graph[computer2].append(computer1)
   def is_fully_connected(self):
       if not self.graph:
           return False
       start_node = next(iter(self.graph))
       visited = set()
       self.dfs(start_node, visited)
       return len(visited) == len(self.graph)

# test: Create a network graph
network = NetworkGraph()
 
# Add computer vertices and connect them
network.add_computer("A")
network.add_computer("B")
network.add_connection("A", "B")
 
# Verify is all computers are connected
print(is_fully_connected(network))
 
# Add more computers to the network and connect them
network.add_computer("C")
network.add_computer("C")
network.add_computer("C", "D")

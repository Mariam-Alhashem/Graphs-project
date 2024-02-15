#graph class
class Graph:
    def __init__(self):
        self.graph = {} # the graph has a dictionary of memebers

    # method to add new member (name + any info)
    def add_member(self, member):
        if member not in self.graph:
            self.graph[member] = [] # each member has a list of relationships
      
    #method to add relationship between members
    def add_relationship(self, member1, member2):
      if member1 in self.graph and member2 in self.graph:
          if member2 not in self.graph[member1]:
              self.graph[member1].append(member2)
          if member1 not in self.graph[member2]:
              self.graph[member2].append(member1)
          else:
              print("One or both members not found in the network.")
          
    #method to find friends of a member (list of all the friends)
    def find_friends(self,member):
      print(self.graph[member])
  
  #method to find a path between 2 members
#method to find a path between 2 members
    def find_path(self, member1, member2):
        if member1 not in self.graph or member2 not in self.graph:
            print("One or both members not found in the network.")
            return -1
        visited = set()
        queue = [(member1, 0)]  # Queue of tuples (member, distance)
        while queue:
            current_member, distance = queue.pop(0)
            if current_member == member2:
                return distance
            visited.add(current_member)
            for friend in self.graph[current_member]:
                if friend not in visited:
                    queue.append((friend, distance + 1))

        
# test 
social_networks = Graph()

social_networks.add_member("mariam")
social_networks.add_member("shahgul")
social_networks.add_member("sijie")

social_networks.add_relationship("mariam", "shahgul")
social_networks.add_relationship("sijie", "shahgul")
social_networks.find_friends("mariam")
social_networks.find_friends("shahgul")
social_networks.find_friends("sijie")

# test the path thing
member1 = "mariam"
member2 = "sara"
path_length = social_networks.find_path(member1, member2)

if path_length != -1:
    print(f"There are {path_length} degrees of separation between {member1} and {member2}.")
else:
    print(f"No path found between {member1} and {member2}.")

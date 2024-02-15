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
    def find_path(self, member1, member2):
        if member1 not in self.graph or member2 not in self.graph:
            print("One or both members not found in the network.")
            return -1
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

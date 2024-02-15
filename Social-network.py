#graph class
class Graph:
    def __init__(self):
        self.graph = {} # the graph has a dictionary of memebers

  #method to add new member (name + any info)
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



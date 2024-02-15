#graph class
  print("hello world")
#graph class
class Graph:
    def __init__(self):
        self.graph = {}

#node representing a member 
#node class
def add_member(self, member):
        if member not in self.graph:
            self.graph[member] = []

def add_relationship(self, member1, member2):
        if member1 in self.graph and member2 in self.graph:
            if member2 not in self.graph[member1]:
                self.graph[member1].append(member2)
            if member1 not in self.graph[member2]:
                self.graph[member2].append(member1)
        else:
            print("One or both members not found in the network.")
    


#edge representing a relationship

#method to add new member (name + any info)

#method to add relationship b/w members

#method to find friends of a member (list of all the friends)

#method to find a path between 2 members



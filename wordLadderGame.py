#creat the list to store all the words
list = []
#creat the list to store words that only have three letters
list_three = []
#open the file and append each word line by line
with open('words_alpha.txt','r') as f:
    for line in f:
        line = line.strip()
        list.append(line)
#find the words that only have three letters in list 
for i in list:
    if len(i) == 3:
        list_three.append(i)

class Graph:
    
    def __init__(self):
        self.graph = {}
        
    #find the neighbors
    def find_neighbors(base,words):
        neighbors_list = []
        different = 0
        for w in words:
            for i,j in base,w:
                if i != j:
                    different += 1
                if different == 2:
                    break
            if different == 1:
                neighbors_list.append(w)
        return the neighbors_list
        
    def add_edge(self, word1, word2):
        if word1 not in self.graph:
            self.graph[word1] = [] 
        if word2 not in self.graph:
            self.graph[word2] = [] 
        self.graph[word1].append(word2)
        self.graph[word2].append(word1)
        
    def get_neighbors(self, word):
        return self.graph.get(word, [])
        
    def find_path(self, word1, word2):
       if word1 not in self.graph or word2 not in self.graph:
           print("One or both words not found in the list.")
           return -1
       visited = set()
       queue = [(word1, 0)]  # Queue of tuples (member, distance)
       while queue:
           current_word, distance = queue.pop(0)
           if current_word == word2:
               return distance
           visited.add(current_word)
           for neighbor in self.get_neighbors(current_word):
               if neighbor not in visited:
                   queue.append((neighbor, distance + 1))

def build_graph(word_list):
    graph = Graph()
    for a in word_list:
        
        for w in word_list:
            different = 0
            for i in range(len(w)):
                if a[i] != w[i]:
                    different += 1
                if different == 2:
                    break
            if different == 1:
                graph.add_edge(a,w)
    return graph

graph = build_graph(list_three)
start_word = input('input the start word')
end_word = input('input the end word')
distance = graph.find_path(start_word,end_word)
print(distance)

list = []
list_three = []
with open('words_alpha.txt','r') as f:
    for line in f:
        line = line.strip()
        list.append(line)
for i in list:
    if len(i) == 3:
        list_three.append(i)
print(list_three[1])
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
            neighbors.append(w)

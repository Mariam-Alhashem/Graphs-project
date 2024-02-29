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

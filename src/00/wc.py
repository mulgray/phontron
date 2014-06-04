counts = {}

#file = open('../test/00-input.txt')
file = open('../data/wiki-en-train.word')

for line in file:
    words = line.split(" ")
    
    for w in words:
        w = w.strip()
        if w in counts:
            counts[w] = counts[w] + 1
        else:
            counts[w] = 1

file.close()

for w in counts:
    print w + '\t' + str(counts[w])
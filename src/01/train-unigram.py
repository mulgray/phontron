counts = {}
total_count = 0

training_file = open('../test/01-train-input.txt')
#training_file = open('../data/wiki-en-train.word')

for line in training_file:
    words = line.split(' ')
    words.append('</s>')
    for word in words:
        word = word.strip()
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
        total_count = total_count + 1

training_file.close()

model_file = open('model', 'w')
for word, count in counts.items():
    probability = float(counts[word])/total_count
    print >> model_file, "%s\t%1.6f" % (word, probability)

model_file.close()
import math

lambda1 = 0.95
lambdaunk = 1-lambda1
V = 1000000
W = 0
H = 0
unk = 0

probabilities = {}

model_file = open('model')

# load model
for line in model_file:
    w, P = line.split('\t')
    probabilities[w] = float(P)

model_file.close()

test_file = open('../test/01-test-input.txt')
#test_file = open('../data/wiki-en-test.word')

# print eval
for line in test_file:
    words = line.split(' ')
    words.append('</s>')
    for w in words:
        w = w.strip()
        W = W + 1
        P = lambdaunk / V
        if probabilities.has_key(w):
            P = P + lambda1 * probabilities[w]
        else:
            unk = unk + 1
        H = H - math.log(P, 2)

print "entropy = %1.6f" % (H/W)
print "coverage = %1.6f" % (float(W-unk)/W)
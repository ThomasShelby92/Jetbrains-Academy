import nltk
import random
# Write your code here
file_name = input()

def punct(a):
    punctuation = ["?", "!", "."]
    for i in punctuation:
        if i in a[len(a)-1]:
            return 1
    return 0

def punct2(a):
    punctuation = ["?", "!", "."]
    for i in punctuation:
        if i in a:
            return 1
    return 0



def head1():
    global head
    head = random.choice(list(head_tail))
    while head[0].isupper() != 1:
        head = random.choice(list(head_tail))
        while punct2(head) == 1:
            head = random.choice(list(head_tail))



punctuation = ["?", "!", "."]
f = open(file_name, "r", encoding="utf-8")
g = f.read()
f.close()
g = nltk.WhitespaceTokenizer().tokenize(g)
g1 = nltk.FreqDist(g).N()
g2 = nltk.FreqDist(g).B()
bigrams = list(nltk.trigrams(g))


head_tail = {}
for h1,h2, tail in bigrams:
    head = h1 + " " + h2
    head_tail.setdefault(head, []).append(tail)
ok = 1
head = " "
for j in range(0,10):
    head1()
    sent = head
    while len(sent.split()) < 5:
        tails = nltk.Counter(head_tail[head])
        for tail, count in tails.most_common(1):
            sent += " " + tail
            s = sent.split()
            s = s[-2] + " " + s[-1]
            head = "".join(s)

    while True:
        if punct(head) == 1:
            break
        ok = 1
        tails = nltk.Counter(head_tail[head])
        for tail, count in tails.most_common(1):
            sent += " " + tail
            s = sent.split()
            s = s[-2] + " " + s[-1]
            head = "".join(s)
            if punct(tail) == 1:
                ok = 0
                break
        if ok == 0:
            break
    print(sent)
    sent = ""


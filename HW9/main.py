import sqlite3 as sqlite
import re
import math
import os


def getwords(doc):
    splitter = re.compile('\W+')
    words = [s.lower() for s in splitter.split(doc)
             if len(s) > 2 and len(s) < 20]
    uniq_words = dict([(w, 1) for w in words])
    return uniq_words


class basic_classifier:

    def __init__(self, getfeatures, filename=None):
        self.fc = {}
        self.cc = {}
        self.getfeatures = getfeatures

    def incf(self, f, cat):
        self.fc.setdefault(f, {})
        self.fc[f].setdefault(cat, 0)
        self.fc[f][cat] += 1

    def incc(self, cat):
        self.cc.setdefault(cat, 0)
        self.cc[cat] += 1

    def fcount(self, f, cat):
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0

    def catcount(self, cat):
        if cat in self.cc:
            return float(self.cc[cat])
        return 0

    def totalcount(self):
        return sum(self.cc.values())

    def categories(self):
        return self.cc.keys()

    def train(self, item, cat):
        features = self.getfeatures(item)
        for f in features:
            self.incf(f, cat)
        self.incc(cat)

    def fprob(self, f, cat):
        if self.catcount(cat) == 0:
            return 0
        return self.fcount(f, cat)/self.catcount(cat)

    def weightedprob(self, f, cat, prf, weight=1.0, ap=0.5):
        basicprob = prf(f, cat)
        totals = sum([self.fcount(f, c) for c in self.categories()])
        bp = ((weight*ap)+(totals*basicprob))/(weight+totals)
        return bp


class naivebayes(basic_classifier):

    def __init__(self, getfeatures):
        basic_classifier.__init__(self, getfeatures)
        self.thresholds = {}

    def docprob(self, item, cat):
        features = self.getfeatures(item)
        p = 1
        for f in features:
            p *= self.weightedprob(f, cat, self.fprob)
        return p

    def prob(self, item, cat):
        catprob = self.catcount(cat)/self.totalcount()
        docprob = self.docprob(item, cat)
        return docprob*catprob

    def setthreshold(self, cat, t):
        self.thresholds[cat] = t

    def getthreshold(self, cat):
        if cat not in self.thresholds:
            return 1.0
        return self.thresholds[cat]

    def classify(self, item, default=None):
        probs = {}
        max = 0.0
        for cat in self.categories():
            probs[cat] = self.prob(item, cat)
            if probs[cat] > max:
                max = probs[cat]
                best = cat
        for cat in probs:
            if cat == best:
                continue
            if probs[cat]*self.getthreshold(best) > probs[best]:
                return default
        return best


all_training_ontopic_files = os.listdir('training_data\ontopic')
all_training_offtopic_files = os.listdir('training_data\offtopic')
all_testing_ontopic_files = os.listdir('testing_data\ontopic')
all_testing_offtopic_files = os.listdir('testing_data\offtopic')

list_train_data = []

for item in all_training_ontopic_files:
    fd = open('training_data\ontopic\\' + item, 'r', encoding="utf8")
    text = fd.read()
    train_data = {'text': text, 'class': 'on topic'}
    list_train_data.append(train_data)

for item in all_training_offtopic_files:
    fd = open('training_data\offtopic\\' + item, 'r', encoding="utf8")
    text = fd.read()
    train_data = {'text': text, 'class': 'off topic'}
    list_train_data.append(train_data)


def sampletrain(cl):
    for item in list_train_data:
        cl.train(item['text'], item['class'])
    

cl = naivebayes(getwords)
sampletrain(cl)

list_testing_ontopic_data = []
for item in all_testing_ontopic_files:
    fd = open('testing_data\ontopic\\' + item, 'r', encoding="utf8")
    text = fd.read()
    train_data = {'text': text, 'class': 'on topic'}
    list_testing_ontopic_data.append(train_data)

list_testing_offtopic_data = []
for item in all_testing_offtopic_files:
    fd = open('testing_data\offtopic\\' + item, 'r', encoding="utf8")
    text = fd.read()    
    train_data = {'text': text, 'class': 'off topic'}
    list_testing_offtopic_data.append(train_data)

print(cl.classify(list_testing_ontopic_data[0]['text'], default='unknown'))
print(cl.classify(list_testing_ontopic_data[1]['text'], default='unknown'))
print(cl.classify(list_testing_ontopic_data[2]['text'], default='unknown'))
print(cl.classify(list_testing_ontopic_data[3]['text'], default='unknown'))
print(cl.classify(list_testing_ontopic_data[4]['text'], default='unknown'))

print(cl.classify(list_testing_offtopic_data[0]['text'], default='unknown'))
print(cl.classify(list_testing_offtopic_data[1]['text'], default='unknown'))
print(cl.classify(list_testing_offtopic_data[2]['text'], default='unknown'))
print(cl.classify(list_testing_offtopic_data[3]['text'], default='unknown'))
print(cl.classify(list_testing_offtopic_data[4]['text'], default='unknown'))

import re
import string
import nltk
from nltk.stem.porter import PorterStemmer

class Word():

    def __init__(self, word, count = 1, prob = 0):
        self.word = word
        self.count = count
        self.prob = prob

    def get_count(self):
        return self.count

    def incr_count(self):
        self.count += 1

    def set_prob(self, prob):
        self.prob = prob

    def get_prob(self):
        return self.prob

class Topic():

    def __init__(self):
        self.words = {}
        self.word_count = 0
        self.topic_prob = 0
        self.count = 0

    def add_word(self, word):
        self.word_count += 1
        if (word in self.words):
            self.words[word].incr_count()
        else:
            self.words[word] = Word(word) 

    def create_prob_dist(self):
        for word in self.words:
            prob = self.words[word].get_count() / self.word_count
            self.words[word].set_prob(prob)

    def get_word_given_topic(self, word):
        if (word in self.words):
            return self.words[word].get_prob()
        else:
            return PWORDTOPIC 

    def incr_count(self):
        self.count += 1

    def get_count(self):
        return self.count

    def get_prob(self):
        return self.topic_prob

    def set_prob(self, prob):
        self.topic_prob = prob

class Bayes():

    def __init__(self):
        self.db = [Topic() for i in range(250)]
        self.num_ques = 0

    def insert_question(self, question, topics):
        self.num_ques += 1
        words = question.split()
        for topic in topics:
            for word in words:
                if (word in common_words):
                    continue
                if (word in COUNTS):
                    COUNTS[word] += 1
                else:
                    COUNTS[word] = 1
                self.db[topic].add_word(word)
            self.db[topic].incr_count()

    def create_probability_db(self):
        for topic in self.db:
            topic.create_prob_dist()
            topic.set_prob(topic.get_count() / self.num_ques)

    def label_query(self, query):
        # to calculate P(topic | words)
        prob = [self.db[t].get_prob() for t in range(250)]  # set to P(topic)
        words = query.split()
        for t in range(250):
            # find out P(topic).P(word | topic)
            for word in words:
                if (word in common_words):
                    continue
                prob[t] *= self.db[t].get_word_given_topic(word)   
                if (word in COUNTS):
                    prob[t] /= COUNTS[word] / TOTAL_WORDS
                else:
                    prob[t] /= PWORDTOPIC 

        final_list = [str(i[0]) for i in sorted(enumerate(prob), key=lambda 
                                                x:x[1], reverse=True)]
        return (' '.join(final_list[0 : 10]) + '\n')


COUNTS = {}
# I/O code
bayes = Bayes()

#####################
# cleaning the data #
#####################

common_eng = open('common_eng_words.txt', 'r')
common_words = set()
for line in common_eng.readlines():
    common_words.add(line.split()[1])

intab = string.punctuation
outtab = ' ' * len(intab)
punctuation_translator = ''.maketrans(intab, outtab)

stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def clean_data(s):
    s = s.lower()
    s = s.translate(punctuation_translator)
    tokens = nltk.word_tokenize(s)
    stems = stem_tokens(tokens, stemmer)
    return ' '.join(stems) 

tmp = set()
for word in common_words:
    word = clean_data(word)
    tmp.add(word)

common_words = set(tmp)

reg = '[0-9]'

file = open('labeler_sample.in', 'r')
t, e = map(int, file.readline().split())
TOTAL_WORDS = t * 8 # assuming 8 words per question on an average
for test in range(t):
    topics = list(map(int, file.readline().split()))
    del topics[0]
    question = str(file.readline())
    question = clean_data(question)
    question = re.sub(reg, ' ', question)
    bayes.insert_question(question, topics)

bayes.create_probability_db()
PWORDTOPIC = 1 / len(COUNTS)
outfile = open('labeler_sample.out', 'w')
for q in range(e):
    query = str(file.readline())
    query = clean_data(query)
    query = re.sub(reg, ' ', query)
    outfile.write(bayes.label_query(query))
file.close()
outfile.close()

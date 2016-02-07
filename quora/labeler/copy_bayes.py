#!/usr/bin/python3

########################################
# This program will run with python3.4 #
########################################
import re

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
            return 1 / TOTAL_WORDS 

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
        self.db = [Topic() for i in range(MAX_TOPICS)]
        self.num_ques = 0

    def insert_question(self, question, topics):
        self.num_ques += 1
        words = question.split()
        del words[0]
        for topic in topics:
            for word in words:
                word = word.lower()
                if (word in common_words):
                    continue
                self.db[topic].add_word(word)
            self.db[topic].incr_count()

    def create_probability_db(self):
        for topic in self.db:
            topic.create_prob_dist()
            topic.set_prob(topic.get_count() / self.num_ques)

    def label_query(self, query):
        # to calculate P(topic | words)
        prob = [self.db[t].get_prob() for t in range(MAX_TOPICS)]  # set to P(topic)
        words = query.split()
        for t in range(MAX_TOPICS):
            # find out P(topic).P(word | topic)
            for word in words:
                word = word.lower()
                if (word in common_words):
                    continue
                prob[t] *= self.db[t].get_word_given_topic(word)   

        final_list = [str(i[0]) for i in sorted(enumerate(prob), key=lambda 
                                                x:x[1], reverse=True)]
        return (' '.join(final_list[0 : 10]))


MAX_TOPICS = 250
# I/O code
bayes = Bayes()
# punctuation and numbers, shouldn't affect our classification into topics
reg = '[\'\",.(\'\.)!@#$%\?\-\+:;0-9\/\(\[\{\)\]\}]'
# common english words, shouldn't affect our classification so we can skip these
common_words = {'and', 'or', 'no', 'our', 'it', 'can', 'when', 'his', 'back', 
                'her', 'out', 'we', 'know', 'see', 'your', 'from', 'this', 
                'their', 'first', 'have', 'people', 'only', 'come', 'about', 
                'she', 'my', 'go', 'most', 'if', 'work', 'want', 'be', 'what', 
                'as', 'they', 'its', 'these', 'any', 'so', 'how', 'of', 'with', 
                'which', 'not', 'new', 'now', 'well', 'I', 'me', 'also', 
                'after', 'get', 'over', 'for', 'year', 'use', 'take', 'good', 
                'than', 'that', 'just', 'us', 'by', 'an', 'look', 'like', 'two', 
                'but', 'will', 'into', 'on', 'time', 'make', 'give', 'at', 
                'some', 'say', 'would', 'do', 'a', 'you', 'him', 'day', 'who', 
                'could', 'to', 'them', 'he', 'think', 'in', 'all', 'then', 
                'way', 'the', 'one', 'there', 'because', 'other', 'even', 'up'}
t, e = map(int, input().split())
TOTAL_WORDS = t * 0.3   # Used later to identify P(word | topic) for a query word that is not in our database
                        # The multiplier is the most optimal found for this set.
                        # Otherwise a general rule would be to use the total number of words seen in the 
                        # training set. Hence t * 8     (considering 8 words on an average 
                        # in each training query). The results do not differ 
                        # very much.
for test in range(t):
    topics = list(map(int, input().split()))
    del topics[0]   # no need for the number of topics
    question = str(input())
    question = re.sub(reg, ' ', question)   # remove numbers and punctuation
    bayes.insert_question(question, topics) # insert the question into topics

bayes.create_probability_db()   # create conditional probabilities P(word | topic) and P(topic)
for q in range(e):
    query = str(input())
    query = re.sub(reg, ' ', query) # remove numbers and punctuation
    print(bayes.label_query(query)) # label this query

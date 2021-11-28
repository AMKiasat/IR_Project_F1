import codecs

import pandas as pd
from parsivar import Normalizer
from parsivar import Tokenizer
from parsivar import SpellCheck
from parsivar import FindStems
import pickle
import os


# 'IR1_7k_news.xlsx'
# 'content'


def main():
    question = input("I am your google assistance ask me your question:")
    position = dict()
    df = pd.read_excel('IR1_7k_news.xlsx')
    x = df['content']
    title = df['title']
    my_normalizer = Normalizer(statistical_space_correction=True)
    my_tokenizer = Tokenizer()
    my_stemmer = FindStems()
    sw = codecs.open('Stop_words.txt', encoding='utf-8').read().split('\r\n')
    stop_words = dict()
    for i in sw:
        stop_words[i] = 1
    # stemmed = []
    if os.path.isfile('position.pickle'):
        with open('position.pickle', 'rb') as handle:
            position = pickle.load(handle)
    else:
        for i in range(len(x)):
            words = my_tokenizer.tokenize_words(my_normalizer.normalize(x[i]))
            # tmp = []
            for j in range(len(words)):
                if words[j] not in stop_words:
                    b = my_stemmer.convert_to_stem(words[j])
                    # tmp.append(b)
                    if b not in position:
                        position[b] = dict()
                    if i not in position[b]:
                        position.get(b)[i] = list()
                    position.get(b).get(i).append(j)
            # stemmed.append(tmp)
        with open('position.pickle', 'wb') as handle:
            pickle.dump(position, handle, protocol=pickle.HIGHEST_PROTOCOL)
    question_words = my_tokenizer.tokenize_words(my_normalizer.normalize(question))
    clean_q_words = []
    q_w_locations = []
    for i in range(len(question_words)):
        if question_words[i] not in stop_words:
            b = my_stemmer.convert_to_stem(question_words[i])
            q_w_locations.append(position[b])
            clean_q_words.append(b)
    # print(clean_q_words)
    if len(q_w_locations) == 1:
        for key in q_w_locations[0].keys():
            print(title[key])
        return
    answers = [q_w_locations]
    # print(answers)
    for h in range(len(clean_q_words) - 1):
        t = []
        # print(h)
        for i in range(len(answers[h]) - 1):
            tmp = []
            f_keys = []
            s_keys = []
            for key in answers[h][i].keys():
                f_keys.append(key)
            for key in answers[h][i + 1].keys():
                s_keys.append(key)
            new_docs = dict()
            for j in f_keys:
                for l in s_keys:
                    if j == l:
                        new_pos = []
                        for p1 in answers[h][i].get(j):
                            for p2 in answers[h][i + 1].get(l):
                                if p1 + 1 == p2:
                                    new_pos.append(p2)
                        new_docs[j] = new_pos
            t.append(new_docs)
        answers.append(t)
        # print(t)
    # print(answers[0])
    # print(answers[1])
    printed_titles = set()
    # print(len(answers))
    for i in range((len(answers) - 1), -1, -1):
        # print(i)
        for j in range(len(answers[i])):
            for k in answers[i][j].keys():
                if len(answers[i]) != 0:
                    if k not in printed_titles:
                        print(title[k])
                        printed_titles.add(k)


if __name__ == '__main__':
    main()

# انتهای پیام
# براق محمد جواد مداح
# بین‌الملل
# تیم فوتبال استقلال با برتری

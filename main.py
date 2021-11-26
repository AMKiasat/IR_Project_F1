import codecs

import pandas as pd
from parsivar import Normalizer
from parsivar import Tokenizer
from parsivar import SpellCheck
from parsivar import FindStems
from pandas import ExcelWriter
from pandas import ExcelFile


# 'IR1_7k_news.xlsx'
# 'content'


def main():
    question = input("I am your google assistance ask me your question:")
    unique = []
    position = []
    df = pd.read_excel('IR1_7k_news.xlsx')
    x = df['content']
    title = df['title']
    my_normalizer = Normalizer(statistical_space_correction=True)
    my_tokenizer = Tokenizer()
    my_stemmer = FindStems()
    stop_words = codecs.open('Stop_words.txt', encoding='utf-8').read().split('\r\n')
    stemmed = []
    for i in range(len(x)):
        words = my_tokenizer.tokenize_words(my_normalizer.normalize(my_normalizer.normalize(x[i])))
        tmp = []
        for j in range(len(words)):
            if stop_words.count(words[j]) == 0:
                b = my_stemmer.convert_to_stem(words[j])
                tmp.append(b)
                if unique.count(b) == 0:
                    unique.append(b)
                    tm = [i, j]
                    t = [tm]
                    position.append(t)
                else:
                    a = unique.index(b)
                    tm = [i, j]
                    position[a].append(tm)
        stemmed.append(tmp)
        print(tmp)
    question_words = my_tokenizer.tokenize_words(my_normalizer.normalize(my_normalizer.normalize(question)))
    clean_q_words= []
    for i in range(len(question_words)):
        if stop_words.count(question_words[i]) == 0:
            clean_q_words.append(my_stemmer.convert_to_stem(question_words[i]))
    q_w_locations = []
    for i in range(len(clean_q_words)):
        for j in range(len(unique)):
            if clean_q_words[i] == unique[j]:
                q_w_locations.append(position[j])
                print(position[j])
    a = []
    if len(clean_q_words) == 1:
        for i in range(len(q_w_locations[0])):
            if(a.count(q_w_locations[0][i][0]) == 0):
                print(title[q_w_locations[0][i][0]])
                a.append(q_w_locations[0][i][0])
    # for i in range(len(q_w_locations)):
    #     for j in range(len(q_w_locations[i])):
    #         for k in range(i,len(q_w_locations)):
    #             for l in range(len(q_w_locations[k])):
    #                 if (q_w_locations[i][j][0] == q_w_locations[k][l][0] and q_w_locations[i][j][1] + 1 == q_w_locations[k][l][1])



if __name__ == '__main__':
    main()

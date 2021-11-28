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

    print(position['سلام'])
    print(position['خوبی'])

    question_words = my_tokenizer.tokenize_words(my_normalizer.normalize(question))
    clean_q_words = []
    q_w_locations = []
    for i in range(len(question_words)):
        if question_words[i] not in stop_words:
            b = my_stemmer.convert_to_stem(question_words[i])
            q_w_locations.append(position[b])
            clean_q_words.append(b)

    for key in q_w_locations[0].keys():
        print(title[key])
    # print(q_w_locations[0])
    # print(q_w_locations[1])
    # if len(q_w_locations) == 1:
    #     print(title[q_w_locations.keys(0)])
    #     return
    # answers = [q_w_locations]
    # for h in range(len(clean_q_words) - 1):
    #     t = []
    #     print(h)
    #     for i in range(len(answers[h]) - 1):
    #         tmp = []
    #         for j in range(len(answers[h][i])):
    #             for l in range(len(answers[h][i + 1])):
    #                 if (answers[h][i][j][0] == answers[h][i + 1][l][0] and answers[h][i][j][1] + 1 == answers[h][i + 1][l][1]):
    #                     tmp.append(answers[h][i + 1][l])
    #                     print(answers[h][i + 1][l])
    #                     # print(stemmed[answers[h][i + 1][l][0]][answers[h][i + 1][l][1]])
    #         t.append(tmp)
    #         print(t)
    #     answers.append(t)
    #     print("shod")
    #     h = h + 1
    # printed_titles = []
    # print(len(answers))
    # for i in range((len(answers) - 1), -1, -1):
    #     print(i)
    #     for j in range(len(answers[i])):
    #         for k in range(len(answers[i][j])):
    #             if len(answers[i]) != 0:
    #                 if printed_titles.count(answers[i][j][k][0]) == 0:
    #                     print(title[answers[i][j][k][0]])
    #                     printed_titles.append(answers[i][j][k][0])


if __name__ == '__main__':
    main()

# انتهای پیام
# براق محمد جواد مداح

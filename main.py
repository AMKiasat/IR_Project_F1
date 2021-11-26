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
    unique = []
    position = []
    df = pd.read_excel('IR1_7k_news.xlsx')
    x = df['content']
    my_normalizer = Normalizer(statistical_space_correction=True)
    my_tokenizer = Tokenizer()
    my_stemmer = FindStems()
    stop_words = codecs.open('Stop_words.txt', encoding='utf-8').read().split('\r\n')
    print(stop_words)
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
    print(unique)
    print(position)

if __name__ == '__main__':
    main()

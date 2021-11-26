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
    normalized = []
    df = pd.read_excel('IR1_7k_news.xlsx')
    x = df['content']
    my_normalizer = Normalizer(statistical_space_correction=True)
    my_tokenizer = Tokenizer()
    my_stemmer = FindStems()

    for i in x:
        normalized.append(my_normalizer.normalize(i))

    words = []
    for i in normalized:
        words.append(my_tokenizer.tokenize_words(my_normalizer.normalize(i)))
    # print(words[0])

    stemmed = []
    for i in range(len(words)):
        tmp = []
        for j in words[i]:
            tmp.append(my_stemmer.convert_to_stem(j))
        stemmed.append(tmp)
    print(stemmed[0])


if __name__ == '__main__':
    main()

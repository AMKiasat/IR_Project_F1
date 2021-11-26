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
    words = []
    stemmed = []
    for i in x:
        words = my_tokenizer.tokenize_words(my_normalizer.normalize(my_normalizer.normalize(i)))
        tmp = []
        for j in words:
            tmp.append(my_stemmer.convert_to_stem(j))
        stemmed.append(tmp)
        print(stemmed.pop())
    

if __name__ == '__main__':
    main()

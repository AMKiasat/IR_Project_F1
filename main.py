import pandas as pd
from parsivar import Normalizer
from parsivar import Tokenizer
from pandas import ExcelWriter
from pandas import ExcelFile

# 'IR1_7k_news.xlsx'
# 'content'
def main():
    df = pd.read_excel('IR1_7k_news.xlsx')
    x = df['content']
    my_normalizer = Normalizer()
    my_tokenizer = Tokenizer()
    words = my_tokenizer.tokenize_words(my_normalizer.normalize(x[0]))
    print(words)


if __name__ == '__main__':
    main()

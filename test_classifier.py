# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:31:06 2019

@author: 27183
"""
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

def preprocess(doc):
    #tokenize the doc and remove the punctuation.
    doc['text'] = [entry.lower() for entry in doc['text']]
    # remove punctuation
    for punctuation in string.punctuation:
        doc['text'] = [entry.replace(punctuation, ' ') for entry in doc['text']] 
    doc['text'] = [word_tokenize(entry) for entry in doc['text']]
    
    for index,entry in enumerate(doc['text']):
        Final_words = []
        ps = PorterStemmer()
        for word in entry:
            if word not in stopwords.words('english'):
                word_Final = ps.stem(word)
                Final_words.append(word_Final)
        doc.loc[index,'text_final'] = str(Final_words)
    # remove stop words
    '''
    doc = [word for word in doc if word not in list(stopwords.words('english'))]
    output_str = []
    ps = PorterStemmer()
    for word in doc:
        output_str.append(ps.stem(word))
    '''
    return doc


def read_csv():
    Corpus = pd.read_csv("avvo_questions_by_practice_area.csv",encoding='latin-1')
    Corpus_new = Corpus[1:50]
    Corpus_new = Corpus_new.append(Corpus[1000:1050])
    Corpus_new = Corpus_new.append(Corpus[2000:2050])
    #Corpus = preprocess(Corpus)

    print("done")
    



if __name__ == '__main__':
    read_csv()
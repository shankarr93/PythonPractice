import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np

#Nltk English stopwords saved to variable stop.
stop = stopwords.words('english')

#Reading the CSV file as Pandas DataFrame.
data= pd.read_csv('Input_RFP - Requirements.csv', encoding='iso-8859-1')

#Tokenizing and Removing stopwords from the Requirements set.
data['token'] = [word_tokenize(txt) for txt in data['Requirement']]
data['clean_tokens'] = data['token'].apply(lambda w: [a for a in w if not a in stop])

#Jaccard's Similarity function
def jaccard_similarity(sent1, sent2):
    intersection = set(sent1).intersection(set(sent2))
    union = set(sent1).union(set(sent2))
    return len(intersection)/len(union)

#The New Requirement statement is taken from the user and its tokenized and stopwords are being removed.
new_sent= input('Enter the New Requirement.')
new_tok=word_tokenize(new_sent)
new_clean_tok=[w for w in new_tok if not w in stop]

#Correlation of the New Requirement with previous requirement is computed and is put in list.
corr=[]
for doc in data['clean_tokens']:
  corr.append(jaccard_similarity(doc, new_clean_tok))

#Correlation value 0 being lowest and 1 being highest.
#With the below code correlation of the New Requirement with previous requirements are computed.
#The best correlation value is taken and the respective previous requirement is printed.
val=max(corr)
idx=corr.index(max(corr))
print('The New Requirement is similar to below old previous Requirement with a correlation of :',val)
print(data['Requirement'][idx])

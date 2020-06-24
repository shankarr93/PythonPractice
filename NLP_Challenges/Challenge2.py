import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

#Reading the CSV file using Pandas
data=pd.read_csv('ticket_Data.csv')

#Using Vectorization method we are turing the text document into numerical feature vectors.
#This has inbuilt 'english' stopwords that will automatically be removed and it fetchs all the ngrams of range 2 to 4.
#The fit_transform method in converts the documents in 'Description' column to 'Document term Matric'(dtm).
#Since dtm is sparse matrix we convert it to array.
vect=CountVectorizer(stop_words='english', ngram_range=(2,4))
dtm=vect.fit_transform(data['Description']).toarray()

#The dtm rows will be respective document rows as give in the dataset.
#The dtm columns will be the ngrams created from vectorizer.
#We sum the the columns as that will give us Frequency Distribution of ngrams.
print("Shape of the document term matrix:",dtm.shape)
dtm_sum=dtm.sum(axis=0)

#Using Pandas series we create a series for Frequency Distribution.
FDIST=pd.Series(dtm_sum, index=vect.get_feature_names())

#Using Pandas series method we will be able to fetch the top highest used ngrams.
#In the below case we get the top 10 key issues.
print('Below are the top 10 keys issues:')
print(FDIST.nlargest(n=10))

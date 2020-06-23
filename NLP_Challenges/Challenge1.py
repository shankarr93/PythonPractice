import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#Loading inbuilt English stopwords to variable stop
stop=stopwords.words('english')

#Using Pandas to read the CSV file
data = pd.read_csv('ticket_Data.csv')

#Tokenizing and removing stop words
data['tokens_by_row'] = [word_tokenize(txt) for txt in data['Description']]
data['clean_tokens'] = data['tokens_by_row'].apply(lambda sent: [word for word in sent if not word in stop])

#Since the clean tokens are multiple rows of dataset, we collect them in a list 'complete_tokens'
complete_tokens=[]
for row in data['clean_tokens']:
  for element in row:
    complete_tokens.append(element)

#Set operation is used to filter out the repeated tokens
distinct_tokens=set(complete_tokens)


print('Total Distinct tokens given in the data set are:',len(complete))
print('Below are the Distinct Tokens:')
print(distinct_tokens)

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

#Importing datasets
train_df = pd.read_json('https://raw.githubusercontent.com/shankarr93/PythonPractice/master/train.json')
test_df = pd.read_json('https://raw.githubusercontent.com/shankarr93/PythonPractice/master/test.json')

#To convert list of ingredients to string type, and put it in a new column
#Since Countvectorizer needs string input to vectorize.
def convert_to_str(df):

    # string representation of the ingredient list
    df['ingredients_str'] = df.ingredients.astype('str')

    return df

train= convert_to_str(train_df)
test=convert_to_str(test_df)

#Define Input(X) which is all the Ingredients
#Output(y) the cuisine type
X = train.ingredients_str
y = train.cuisine

#Define Input for testing dataset
X_test = test.ingredients_str
 
# Instantiate CountVectorizer and Multinomial Naive Bayes
vect = CountVectorizer()
nb = MultinomialNB()


#Making a Pipline with CountVectorizer and Multinomial Naive Bayes
pipe = make_pipeline(vect, nb)

#Since we are going to use GridSearchCV method for training the dataset, we use param_grid for hyperparameter variation trials.
param_grid = {}
#Since the list of ingredients is converted to text, with the below regex we get individual tokens 
param_grid['countvectorizer__token_pattern'] = [r"\b\w\w+\b", r"'([a-z ]+)'"]
param_grid['multinomialnb__alpha'] = [0.5, 1]

# Passing the pipeline to GridSearchCV for 5 fold crossvalidation.
grid = GridSearchCV(pipe, param_grid, cv=5)

# Fitting the model for training data
grid.fit(X, y)

#Using the Fit Model to predict the Cuisines for the given ingredients in Test dataset.
prediction = grid.predict(X_test)

print('Please find Cusine Prediction results for the test dataset below:')
result=pd.DataFrame({ 'ingredients':test.ingredients, 'cuisine':prediction})
print(result)

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle
import os

def train_model():
    df = pd.read_csv("data.csv")
    category_col =['Sex','Other Problems']
    labelEncoder = preprocessing.LabelEncoder()

    # creating a map of all the numerical values of each categorical labels.
    mapping_dict={}
    for col in category_col:
        df[col] = labelEncoder.fit_transform(df[col])
        le_name_mapping = dict(zip(labelEncoder.classes_, labelEncoder.transform(labelEncoder.classes_)))
        mapping_dict[col]=le_name_mapping
    print(mapping_dict)
    X = df.values[:, 0:8]
    Y = df.values[:,8]

    X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)
    dt_clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                                   max_depth=5, min_samples_leaf=5)
    dt_clf_gini.fit(X_train, y_train)
    y_pred_gini = dt_clf_gini.predict(X_test)

    print ("Desicion Tree using Gini Index\nAccuracy is ", accuracy_score(y_test,y_pred_gini)*100 )

    #creating and training a model
    #serializing our model to a file called model.pkl
    import pickle
    pickle.dump(dt_clf_gini, open(os.path.dirname(os.path.abspath(__file__))+"/model.pkl","wb"))

def load_model():
    model = pickle.load(open(os.path.dirname(os.path.abspath(__file__))+"/model.pkl", 'rb'))
    return model

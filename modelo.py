# -*- coding: utf-8 -*-
"""Iris_Aula - Export Pickle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18N60Duey2me2abRtpeQSiK5mh9Jgz6L0
"""

#!pip install -q scikit-learn==1.3.1
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import datasets
import pickle

iris = datasets.load_iris()
iris.keys()
#print(iris.DESCR)

labels_names = iris.target_names
pickle.dump(labels_names, open('names.pkl','wb'))
nomesiris = pickle.load(open('names.pkl','rb'))
print(nomesiris)

x = iris.data
y = iris.target

#realizando o split da base para teste
from sklearn.model_selection import train_test_split
x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_treino, y_treino)

preditos = clf.predict(x_teste)
print("Preditos:",preditos)
print("Real    :",y_teste)

from sklearn.metrics import accuracy_score
print("Acuracia:", accuracy_score(y_teste,preditos))

pickle.dump(clf, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
print (model.predict([ [5,2,5,2.5] ]))
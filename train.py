# Import der benötigten Bibliotheken
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import pickle

# Laden, Vorbereiten und Splitten der Trainingsdaten
attribute_names = ['variance_wavelet_transformed_image', 'skewness_wavelet_transformed_image', 'curtosis_wavelet_transformed_image', 'entropy_image', 'class']
data = pd.read_csv('data_banknote_authentication.csv.txt', names=attribute_names)
data = data.sample(frac=1)
y_variable = data['class']
x_variables = data.loc[:, data.columns != 'class']
x_train, x_test, y_train, y_test = train_test_split(x_variables, y_variable, test_size=0.2)

# Trainieren des besten Baums
classifier = DecisionTreeClassifier() 
tree_para = {'criterion':['gini','entropy'],'max_depth':[i for i in range(1,20)], 'min_samples_split':[i for i in range (2,20)]}
grd_clf = GridSearchCV(classifier, tree_para, cv=5)
grd_clf.fit(x_variables, y_variable)
model_with_best_tree_parameters = grd_clf.best_estimator_
btmodel = model_with_best_tree_parameters.fit(x_train,y_train)

# Trainieren des Random Forest
random_forest_classifier = RandomForestClassifier(n_estimators=10)
rfmodel = random_forest_classifier.fit(x_train,y_train)

# Speichern der Modelle
pickle.dump(rfmodel, open("rfmodel.pickle", 'wb'))
pickle.dump(btmodel, open("btmodel.pickle", 'wb'))
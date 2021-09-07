# Import der benötigten Bibliotheken
import pickle
import pandas as pd

# laden der Modelle
btmodel = pickle.load(open("btmodel.pickle", "rb"))
rfmodel = pickle.load(open("rfmodel.pickle", "rb"))

# laden der Testdaten
testdaten = pd.read_csv("testdaten3.csv", names = ['variance_wavelet_transformed_image', 'skewness_wavelet_transformed_image', 'curtosis_wavelet_transformed_image', 'entropy_image', 'class'])
testdaten = testdaten.loc[:, testdaten.columns != 'class']

# Ausgabe
if btmodel.predict(testdaten) == 0:
    print("Best Tree sagt voraus: Keine Fälscheung")
else:
    print("Best Tree sagt voraus: Fälschung")
if rfmodel.predict(testdaten) == 0:
    print("Random Forest sagt voraus: Keine Fälscheung")
else:
    print("Random Forest sagt voraus: Fälschung")
import pandas as pd

input_file = "../data/listing_paris.csv"

data = pd.read_csv(input_file)
#print(data)

#afficher  les  5 premieres  lignes  
#print(data.head(5))
#
#print(data.describe())

#afficher  les valeurs  nulles  
print(data.isnull().sum())
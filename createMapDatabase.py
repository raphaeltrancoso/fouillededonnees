# createMapDatabase.py
#
# Authors :
# 	Raphael Trancoso
# 	Cedric Laguerre 
#
# Projet Fouille de Données 
# Sujet : trafic réseaux ferroviaires Paris
#
# Créé une nouvelle Base de Données nécessaire pour le projet

import pandas as pd

data = pd.read_csv('trafic-annuel-entrant-par-station-du-reseau-ferre-2016.csv', sep = ';')
data2 = pd.read_csv('positions-geographiques-des-stations-du-reseau-ratp.csv', sep = ';')

del data['Rang']
del data['Ville']
del data['Arrondissement pour Paris']
del data['Correspondance_2']
del data['Correspondance_3']
del data['Correspondance_4']
del data['Correspondance_5']
del data['Column 12']
del data['Column 13']
del data['Column 14']
del data['Column 15']
del data2['stop_id']
del data2['stop_desc']
del data2['code_INSEE']
del data2['departement']

# count=0
# for row in data.iterrows():
# 	count=count+1
# print(count)

# for row in data.iterrows():
# 	for row2 in data2.iterrows():
# 		# if(row2[1]['stop_name'].startswith(row[1]['Station'])):
# 		# 	row2[1]['stop_name'] = row[1]['Station']
# 		# 	print(row2[1]['stop_name'])
# 		if row[1]['Station'] in row2[1]['stop_name']:
# 			row2[1]['stop_name'] = row[1]['Station']
# 			print(row2[1]['stop_name'])

data2.drop_duplicates(['stop_name'], keep='last')
print(data2)

newDB = pd.merge(data, data2, left_on='Station', right_on='stop_name', how='left')
newDB.to_csv("./mapDatabase.csv", sep=';', index=False)
# print(newDB)
# print(newDB)
count=0
for row in newDB.iterrows():
	count=count+1
print(count)

# .index()
# .find()
# .startswith()
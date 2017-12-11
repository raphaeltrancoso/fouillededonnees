# Authors :
# 	Raphael Trancoso
# 	Cedric Laguerre 
#
# Projet Fouille de Données 
# Sujet : trafic réseaux ferrés Paris
#
# Données statistiques diverses concernant le trafic 
# des réseaux ferrés parisien

# utilisation de la libraire pandas
import pandas as pd
import numpy as np
import scipy as sp
import sklearn as skl

import matplotlib.pyplot as plt
import matplotlib as matplot
import seaborn as sns


# lit le fichier de données de type csv
data = pd.read_csv('trafic-annuel-entrant-par-station-du-reseau-ferre-2016.csv', sep = ';')

# suppression des colonnes inutiles
del data['Column 12']
del data['Column 13']
del data['Column 14']
del data['Column 15']
new_columns = data.columns.values; 
new_columns[4] = 'Ligne'; 
data.columns = new_columns

# moyenne du trafic annuel de toutes les lignes dans Paris
average_traffic_all = data['Trafic'].mean()

# on prend la colonne du type de réseau ferré (RER ou métro)
network = data.groupby('Réseau')
# moyennes du trafic annuel pour les RER et métros
average_traffic_RER = network.get_group('RER')['Trafic'].mean()
average_traffic_M = network.get_group('Métro')['Trafic'].mean()

# on prend la colonne du nom du reseau ferré
network = data.groupby('Ligne')
# moyennes du trafic annuel pour chaque ligne
average_traffic_RERA = network.get_group('A')['Trafic'].mean()
average_traffic_RERB = network.get_group('B')['Trafic'].mean()
average_traffic_M1 = network.get_group('1')['Trafic'].mean()
average_traffic_M2 = network.get_group('2')['Trafic'].mean()
average_traffic_M3 = network.get_group('3')['Trafic'].mean()
average_traffic_M3bis = network.get_group('3bis')['Trafic'].mean()
average_traffic_M4 = network.get_group('4')['Trafic'].mean()
average_traffic_M5 = network.get_group('5')['Trafic'].mean()
average_traffic_M6 = network.get_group('6')['Trafic'].mean()
average_traffic_M7 = network.get_group('7')['Trafic'].mean()
average_traffic_M7bis = network.get_group('7bis')['Trafic'].mean()
average_traffic_M8 = network.get_group('8')['Trafic'].mean()
average_traffic_M9 = network.get_group('9')['Trafic'].mean()
average_traffic_M10 = network.get_group('10')['Trafic'].mean()
average_traffic_M11 = network.get_group('11')['Trafic'].mean()
average_traffic_M12 = network.get_group('12')['Trafic'].mean()
average_traffic_M13 = network.get_group('13')['Trafic'].mean()
average_traffic_M14 = network.get_group('14')['Trafic'].mean()

# ne fonctionne pas pour le moment
data_arr = data.loc[(data['Ville'] == 'Paris')]
network = data_arr.groupby('Arrondissement pour Paris')

average_traffic_arr1 = network.get_group(1)['Trafic'].mean()
average_traffic_arr2 = network.get_group(2)['Trafic'].mean()
average_traffic_arr3 = network.get_group(3)['Trafic'].mean()
average_traffic_arr4 = network.get_group(4)['Trafic'].mean()
average_traffic_arr5 = network.get_group(5)['Trafic'].mean()
average_traffic_arr6 = network.get_group(6)['Trafic'].mean()
average_traffic_arr7 = network.get_group(7)['Trafic'].mean()
average_traffic_arr8 = network.get_group(8)['Trafic'].mean()
average_traffic_arr9 = network.get_group(9)['Trafic'].mean()
average_traffic_arr10 = network.get_group(10)['Trafic'].mean()
average_traffic_arr11 = network.get_group(11)['Trafic'].mean()
average_traffic_arr12 = network.get_group(12)['Trafic'].mean()
average_traffic_arr13 = network.get_group(13)['Trafic'].mean()
average_traffic_arr14 = network.get_group(14)['Trafic'].mean()
average_traffic_arr15 = network.get_group(15)['Trafic'].mean()
average_traffic_arr16 = network.get_group(16)['Trafic'].mean()
average_traffic_arr17 = network.get_group(17)['Trafic'].mean()
average_traffic_arr18 = network.get_group(18)['Trafic'].mean()
average_traffic_arr19 = network.get_group(19)['Trafic'].mean()
average_traffic_arr20 = network.get_group(20)['Trafic'].mean()

# affichage des donnees
print("Trafic annuel moyen de tous les réseaux : ", average_traffic_all)
print("Trafic annuel moyen RER dans Paris : ", average_traffic_RER)
print("Trafic annuel moyen de tous les métros : ", average_traffic_M)
print("Trafic annuel moyen du RER A dans Paris : ", average_traffic_RERA)
print("Trafic annuel moyen du RER B dans Paris : ", average_traffic_RERB)
print("Trafic annuel moyen du Metro 1 : ", average_traffic_M1)
print("Trafic annuel moyen du Metro 2 : ", average_traffic_M2)
print("Trafic annuel moyen du Metro 3 : ", average_traffic_M3)
print("Trafic annuel moyen du Metro 3bis : ", average_traffic_M3bis)
print("Trafic annuel moyen du Metro 4 : ", average_traffic_M4)
print("Trafic annuel moyen du Metro 5 : ", average_traffic_M5)
print("Trafic annuel moyen du Metro 6 : ", average_traffic_M6)
print("Trafic annuel moyen du Metro 7 : ", average_traffic_M7)
print("Trafic annuel moyen du Metro 7bis : ", average_traffic_M7bis)
print("Trafic annuel moyen du Metro 8 : ", average_traffic_M8)
print("Trafic annuel moyen du Metro 9 : ", average_traffic_M9)
print("Trafic annuel moyen du Metro 10 : ", average_traffic_M10)
print("Trafic annuel moyen du Metro 11 : ", average_traffic_M11)
print("Trafic annuel moyen du Metro 12 : ", average_traffic_M12)
print("Trafic annuel moyen du Metro 13 : ", average_traffic_M13)
print("Trafic annuel moyen du Metro 14 : ", average_traffic_M14)

# affichage du trafic annuel dans les differents arrondissements
print("Trafic annuel dans le 1er arrondissement de Paris : ", average_traffic_arr1)
print("Trafic annuel dans le 2eme arrondissement de Paris : ", average_traffic_arr2)
print("Trafic annuel dans le 3eme arrondissement de Paris : ", average_traffic_arr3)
print("Trafic annuel dans le 4eme arrondissement de Paris : ", average_traffic_arr4)
print("Trafic annuel dans le 5eme arrondissement de Paris : ", average_traffic_arr5)
print("Trafic annuel dans le 6eme arrondissement de Paris : ", average_traffic_arr6)
print("Trafic annuel dans le 7eme arrondissement de Paris : ", average_traffic_arr7)
print("Trafic annuel dans le 8eme arrondissement de Paris : ", average_traffic_arr8)
print("Trafic annuel dans le 9eme arrondissement de Paris : ", average_traffic_arr9)
print("Trafic annuel dans le 10eme arrondissement de Paris : ", average_traffic_arr10)
print("Trafic annuel dans le 11eme arrondissement de Paris : ", average_traffic_arr11)
print("Trafic annuel dans le 12eme arrondissement de Paris : ", average_traffic_arr12)
print("Trafic annuel dans le 13eme arrondissement de Paris : ", average_traffic_arr13)
print("Trafic annuel dans le 14eme arrondissement de Paris : ", average_traffic_arr14)
print("Trafic annuel dans le 15eme arrondissement de Paris : ", average_traffic_arr15)
print("Trafic annuel dans le 16eme arrondissement de Paris : ", average_traffic_arr16)
print("Trafic annuel dans le 17eme arrondissement de Paris : ", average_traffic_arr17)
print("Trafic annuel dans le 18eme arrondissement de Paris : ", average_traffic_arr18)
print("Trafic annuel dans le 19eme arrondissement de Paris : ", average_traffic_arr19)
print("Trafic annuel dans le 20eme arrondissement de Paris : ", average_traffic_arr20)

# Initialise les couleurs du graphique
color_types = ['#D1302F','#427DBD','#FFCD00','#003CA6','#837902','#6EC4E8','#BE418D',  
                '#FF7E2E','#6ECA97','#FA9ABA','#6ECA97','#E19BDF','#B6BD00','#C9910D','#704b1C', '#007852','#6EC4E8','#62259D']

# Cree le graphique
sns.barplot(x=data['Ligne'],
	order=["A", "B", "1", "2", "3", "3bis", "4", "5", "6", "7", "7bis", "8", "9", "10", "11", "12", "13", "14"], 
	y=data['Trafic'], data=data, palette=color_types).set_title('Repartions des usagers par ligne')

plt.show()



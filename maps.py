# Authors :
# 	Raphael Trancoso
# 	Cedric Laguerre 
#
# Projet Fouille de Données 
# Sujet : trafic réseaux ferrés Paris
#
# Cartographie du trafic parisien par station
# Carte des stations dans Paris (heatmap + scatter) -> fichier html

# utilisation de la libraire pandas
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as matplot

import gmplot

# lit le fichier de données de type csv
data = pd.read_csv('mapDatabase.csv', sep = ';')
# on retire les doublons inutiles
data = data.drop_duplicates(['Station', 'Correspondance_1'])

gmap = gmplot.GoogleMapPlotter.from_geocode("Paris")
# n'affichant pas les points en fonction du traffic pour chaque gare,
# on optera pour une heatmap des stations
gmap.scatter(data['stop_lat'], data['stop_lon'], c='b', s=90, marker=False)
gmap.heatmap(data['stop_lat'], data['stop_lon'], radius=30)
gmap.draw("mymap.html")

# on fixe l'échelle minimum et maximun
minTraffic = data['Trafic'].min()
maxTraffic = data['Trafic'].max()/4
normalize = matplot.colors.Normalize(vmin=minTraffic, vmax=maxTraffic)
# creation de la carte grace aux latitudes et longitudes de chaque stations
# chaque point aura une couleur en fonction de son trafic annuel
mapRATP = data.plot(title="Trafic ferré par station", y='stop_lat', x='stop_lon', c="Trafic", 
	norm=normalize, kind="scatter", label='Trafic', cmap='bwr')

plt.legend()
plt.show()

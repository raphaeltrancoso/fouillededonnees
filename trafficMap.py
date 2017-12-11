# trafficMap.py
#
# Authors :
#   Raphael Trancoso
#   Cedric Laguerre 
#
# Projet Fouille de Données 
# Sujet : trafic réseaux ferrés Paris
#
# Cartographie du trafic parisien par station
# Carte du traffic par station dans Paris -> fichier html

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as matplot

import folium
from folium import plugins

# lit le fichier de données de type csv
data = pd.read_csv('mapDatabase.csv', sep = ';')
# on retire les doublons inutiles
data = data.drop_duplicates(['Station', 'Correspondance_1'])

m = folium.Map(location=[48.864716, 2.349014], 
    zoom_start=12)

for row in data.iterrows():
    lat = row[1]['stop_lat']
    lng = row[1]['stop_lon']
    trafic = row[1]['Trafic']
    station = row[1]['Station'] + " " + str(trafic)
    # rouge
    if(trafic >= 30000000):
    	colorStation = '#ff0000'
    #orange
    elif(trafic >= 20000000):
    	colorStation ='#ff9900'
    #jaune
    elif(trafic >= 10000000):
    	colorStation ='#FFFF00'
    #vert
    elif(trafic >= 5000000):
    	colorStation ='#99ff00'
    #vert lime
    else:
    	colorStation ='#00ff00'
    folium.CircleMarker(location=[lat, lng], radius=trafic/750000,
    	color='black', fill=True, fill_color=colorStation, fill_opacity=0.6,
    	popup=station.replace("'"," "), weight=1).add_to(m)
    # folium.Circle(location=[lat, lng], radius=trafic/100000, 
    # 	color='#ffffff', fill=True, fill_color='#ffffff', fill_opacity=0.9,
    # 	popup=station[0:6]).add_to(m)
plugins.Fullscreen(
    position='topright',
    title='Expand me',
    title_cancel='Exit me',
    force_separate_button=True).add_to(m)
m.save("trafficMap.html")
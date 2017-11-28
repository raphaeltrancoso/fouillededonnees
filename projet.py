# authors :
# 
# Raphael Trancoso
# Cedric Laguerre 
#
# projet Fouille de Données 
# sujet : RER A

from pprint import pprint

import json

json_data = open('ponctualite_mensuelle_rerA.json', 'r')

data = json.load(json_data)

# affiche les champs presents dans fields
for donnees in data[0]['fields']:
	pprint(donnees)

# afficher tout le fichier json
# pprint(data)

json_data.close()
# authors : 
# Raphael Trancoso
# Cedric Laguerre 

from pprint import pprint

import json

json_data = open('ponctualite_mensuelle_rerA.json')

print(type(json_data), json_data)

data = json.load(json_data)
print(type(data))
pprint(data)

json_data.close()
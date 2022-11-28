import json

favourite = {
    "title": "Master and Margarita",
    "year of writing": "1930",
    "autor": 'Michaił Bułhakow',
    "Genre": 'Fantastyka,Satyra,Romans,Powieść',
    "first edition": '1967'
   }

json_file=open('favourite.json', 'w')
json.dump(favourite, json_file, indent=4)

json_file.close()

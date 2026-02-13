import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads (person)
# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print( person_dict)
# Output: ['English', 'French']
print (person_dict['languages'])


import json
person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'
# Obtenemos el objeto json como un diccionario
person_dict = json. loads (person_string)
# Lo imprimimos en formato string manteniendo una indentación de 4 espacios
print(json.dumps (person_dict, indent = 4, sort_keys=True))
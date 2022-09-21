import json

data = {'name': 'Ali',
        'surname': 'Hashemi',
        'age': 20,
        'city': 'Tehran',
        }

# first way:

with open('details.json', 'w') as j_file:
    json.dump(data, j_file)

# second way:

json_values = json.dumps(data)
print(json_values)
print(type(json_values))    # not dictionary


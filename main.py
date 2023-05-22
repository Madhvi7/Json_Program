"""program to fetch the keys from the given json"""
import json

f = open('text.json')

data = json.load(f)
details1 = data['siteDetails']

for i in details1:

    print(i)

f.close()

data_set = []
details2 = data['parametersList']
for item in details2:
    dictionary = {
        "parameterName": item['parameterName'],
        "min_value": item['max'],
        "max_value": item['min'],
        "avg_value": item['avg']
    }
    data_set.append(dictionary)
print(data_set)
json_output = json.dumps(data_set, indent=4)
# Writing to solution json
with open("solution.json", "w") as outfile:
    outfile.write(json_output)
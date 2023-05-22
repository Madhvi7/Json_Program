import json

f = open('text.json')

data = json.load(f)

for i in data['siteDetails']:

    print(i)

f.close()
data_set = []
details = data['parametersList']
for item in details:
    dictionary = {
        "parameterName": item['parameterName'],
        "min_value": item['max'],
        "max_value": item['min'],
        "avg_value": item['avg']
    }
    data_set.append(dictionary)
print(data_set)
json_output = json.dumps(data_set, indent=4)
# writing to sample json
with open("solution.json", "w") as outfile:
    outfile.write(json_output)
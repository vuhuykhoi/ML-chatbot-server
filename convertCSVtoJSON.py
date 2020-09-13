import csv, json

csvFilePath = "chatbot-dataset.csv"
jsonFilePath = "intents_train_data.json"

data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        id = csvRow['id']
        if id != '':
            if id in data:
                if csvRow['patterns']: data[id]['patterns'].append(csvRow['patterns'])
                if csvRow['responses']: data[id]['responses'].append(csvRow['responses'])
            else:
                data[id] = csvRow
                del data[id]['id']
                
                pattern_tmp = data[id]['patterns']
                responses_tmp = data[id]['responses']

                data[id]['tag'] = csvRow['tag']
                data[id]['patterns'] = []
                data[id]['responses'] = []
                data[id]['patterns'].append( pattern_tmp)
                data[id]['responses'].append(responses_tmp)

list_data = []
for key, value in data.items():
    temp = value
    list_data.append(temp)

root = {}
root["intents"] = list_data
print(root)


with open(jsonFilePath,'w') as jsonFile:
    jsonFile.write(json.dumps(root, indent = 4))
import json
dictionary_data = {"a": 1, "b": 2, "VHR-345": ["waqad", "car"]}

name = "VHR-335"
DataList = ['faizyab', 'Motorbike']

dictionary_data[name] = DataList

a_file = open("data.json", "w")
json.dump(dictionary_data, a_file)
a_file.close()

a_file = open("data.json", "r")
output = a_file.read()
print(output)
a_file.close()

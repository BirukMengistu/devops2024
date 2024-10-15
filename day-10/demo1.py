import json
#To parse a JSON string, use the `json.loads()` method:
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)
print(data['name'])

""" Parsing JSON from a File
To parse JSON data from a file, use the `json.load()` method: """

import json
with open('data.json', 'r') as file:
 data = json.load(file)
print(data)
print(data['name'])

""" Converting Python Objects to JSON Strings

To convert a Python object into a JSON string, use the `json.dumps()` method: """

import json
data = {
"name": "John",
"age": 30,
"city": "New York"
}
json_string = json.dumps(data , indent= 2)
print(f'json_string \n {json_string}')

""" Writing JSON Data to a File
To write JSON data to a file, use the `json.dump()` method: """

import json
data1 = {
"name": "John",
"age": 30,
"city": "New York",
"email":'',
"sex":'Male'
}
with open('data.json', 'w') as file:
 json.dump(data1, file)
""" 
 Saving JSON to a File

Using `json.dump()` with the `open()` context manager in write mode: """

data = {"model": "Model X", "year": 2022}
with open("data.json", "w") as f:
 json.dump(data, f)
""" Nested JSON Objects
Consider the following nested JSON data: """

import json
json_string = '''
{
"name": "John",
"age": 30,
"address": {
"street": "123 Main St",
"city": "New York"
},
"skills": ["Python", "Django", "Machine Learning"]
}
'''
data = json.loads(json_string)
print(data['address']['city'])
print(data['skills'][0])

# josn CRUD function Add, update, delete

data['color']='red'
print(f'Add element \n {data}')

#update

data['color']='blue'
data['age']=26
print(f'update element \n {data}')
json_string = '{"model": "Model X", "year": 2022}'
json_data = json.loads(json_string)
print(f'orginal \n {json_data}')
more_json_string = '{"model": "Model S", "color": "Red"}'
more_json_data = json.loads(more_json_string)
json_data.update(more_json_data)

print(f'update \n {more_json_string}')
print('*'*50)

#delete


json_string = '{"model": "Model X", "year": 2022}'
json_data = json.loads(json_string)
del json_data['year']
print(f' del {json_data}') # Output: {'model': 'Model X'}

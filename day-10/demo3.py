""" Handling Exceptions

To handle these exceptions, use a try-except block: """

import json
json_string = """{
       "name": "John", 
       "age": 30, 
       "city": "New York" 
       """
try:
    data = json.loads(json_string)
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")

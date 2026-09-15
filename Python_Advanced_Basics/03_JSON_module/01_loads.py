#used to convert json string into pythin object
import json
json_string = '{ "name": "dikshya","isStudent" : true }'


print(type(json_string))

py_obj = json.loads(json_string)
print(type(py_obj), py_obj)


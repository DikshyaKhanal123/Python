#used to convert python object into json string

import json
py_obj = {
    "name" : "dikshya",
    "address" : "syangja"
}

json_str = json.dumps(py_obj)
print(json_str)
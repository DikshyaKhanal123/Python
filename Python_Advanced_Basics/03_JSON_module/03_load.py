# read data form json file

import json
with open("data.json", "r") as f :
    py_obj = json.load(f)

    print(py_obj)


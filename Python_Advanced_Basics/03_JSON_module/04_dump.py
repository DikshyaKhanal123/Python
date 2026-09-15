#used to write in json file
import json
data = {
    "name": "dikshya",
    "roll" : "123"

}

with open("data.json", "w") as f:
    json.dump(data, f)
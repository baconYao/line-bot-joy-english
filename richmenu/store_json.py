
import json


def write_richId(new_id_info, file="richmenu_id.json"):
    with open(file) as store_info:
        data = json.load(store_info)
        data.append(new_id_info)

    with open(file, "w") as f:
        json.dump(data, f)

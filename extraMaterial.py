import json
import os

def addMaterials(item_name):
    folder_path = "./ingotcraftDataPack/data/minecraft/tags/items"
    file_path = os.path.join(folder_path, "trim_materials.json")

    # Create the subfolder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Check if the file "trim_materials.json" exists in the subfolder
    if os.path.exists(file_path):
        # If it does, merge the new data with the preexisting data
        with open(file_path, "r+") as f:
            data = json.load(f)
            data["values"].append(item_name)
            f.seek(0)
            json.dump(data, f, indent=4)
    else:
        # If it doesn't, create a new file with the initial data in the subfolder
        with open(file_path, "w") as f:
            json.dump({"replace": False, "values": [item_name]}, f, indent=4)

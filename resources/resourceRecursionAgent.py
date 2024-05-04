# The point of this is to take each individual item handed to it and apply the trim to it.
import json
import os


def recursiveAgent(folder_path, item_name, imi, armor_material, armor_type):

    file_path = os.path.join(folder_path, f"{armor_material}_{item_name}.json")

    data = {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": f"minecraft:item/{armor_material}",
            "layer1": f"minecraft:trims/items/{armor_type}_trim_{item_name}"
        }
    }

    # Save the JSON to the file
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    file_path = os.path.join(folder_path, f"{armor_material}.json")
    if os.path.exists(file_path):
        # Load the existing JSON data
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        # Create a new JSON data structure if the file doesn't exist
        data = {
            "parent": "minecraft:item/generated",
            "overrides": [],
            "textures": {
                "layer0": f"minecraft:item/{armor_material}"
            }
        }

    data["overrides"].append({"model": f"minecraft:item/{armor_material}_{item_name}_trim","predicate":{"trim_type": imi}})

    # Save the updated JSON back to the file
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def recursiveWrapper(folder_path, armor_material):
    file_path = os.path.join(folder_path, f"{armor_material}.json")

    with open(file_path, "r") as f:
        data = json.load(f)

    data["overrides"].append({"model": f"minecraft:item/{armor_material}_quartz_trim","predicate":{"trim_type": 0.1}})
    data["overrides"].append({"model": f"minecraft:item/{armor_material}_netherite_trim","predicate":{"trim_type": 0.3}})
    data["overrides"].append({"model": f"minecraft:item/{armor_material}_redstone_trim","predicate":{"trim_type": 0.4}})
    data["overrides"].append({"model": f"minecraft:item/{armor_material}_copper_trim","predicate":{"trim_type": 0.5}})
    data["overrides"].append({"model": f"minecraft:item/{armor_material}_gold_trim","predicate":{"trim_type": 0.6}})
    data["overrides"].append({"model": f"minecraft:item/{armor_material}_emerald_trim","predicate":{"trim_type": 0.7}})
    data["overrides"].append({"model": f"minecraft:item/{armor_material}_diamond_trim","predicate":{"trim_type": 0.8}})
    data["overrides"].append({"model": f"minecraft:item/{armor_material}_lapis_trim","predicate":{"trim_type": 0.9}})
    data["overrides"].append({"model": f"minecraft:item/{armor_material}_amethyst_trim","predicate":{"trim_type": 1.0}})

    # Save the updated JSON back to the file
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

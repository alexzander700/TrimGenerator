import os

from resourceManager import resourceManager
from extraMaterial import addMaterials


def generate_material(item, ingredient, imi, color):
    subfolder = "./ingotcraftDataPack/data/minecraft/trim_material"
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)

    """Generates a JSON file with the given parameters."""
    # Set default values if they are not provided
    item = "Ender Purple" if item == "" else item
    ingredient = "ender_pearl" if ingredient == "" else ingredient
    color = "#032620" if color == "" else color
    imi = 0.001 if imi is None else imi

    # Reformats the item name to remove spaces and capitalization
    item_name = item.replace(" ", "_").lower()

    # Adds the item_name to the extraMaterial program
    addMaterials(ingredient)
    resourceManager(item_name, imi)

    # Creates the JSON file in the subfolder mentioned above
    with open(os.path.join(os.getcwd(), subfolder, f"{item_name}.json"), "w") as json_file:
        json_file.write(f"""{{
            "asset_name": "{item_name}",
            "description": {{
                "color": "{color}",
                "text": "{item} Material"
            }},
            "ingredient": "{ingredient}",
            "item_model_index": {imi}
        }}""")

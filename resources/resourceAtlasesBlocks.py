# This python program will be called by another program with the function "resourceBlocksGen(item_name)"
# `"{item_name}": "trims/color_palettes/{item_name}"` will be added to the "permutations" for every time this file is run.
# If "blocks.json" doesn't exist it should generate with the following text:
#
import json
import os


def resourceBlocksGen(item_name):
    folder_path = "./ingotcraftResourcePack/assets/minecraft/atlases"
    file_path = os.path.join(folder_path, "blocks.json")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if os.path.exists(file_path):
        # Load the existing JSON data
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        # Create a new JSON data structure if the file doesn't exist
        data = {
            "sources": [
                {"type": "directory", "source": "block", "prefix": "block/"},
                {"type": "directory", "source": "item", "prefix": "item/"},
                {"type": "directory", "source": "entity/conduit", "prefix": "entity/conduit/"},
                {"type": "single", "resource": "entity/bell/bell_body"},
                {"type": "single", "resource": "entity/enchanting_table_book"},
                {
                    "type": "paletted_permutations",
                    "textures": [
                        "trims/items/leggings_trim",
                        "trims/items/chestplate_trim",
                        "trims/items/helmet_trim",
                        "trims/items/boots_trim",
                    ],
                    "palette_key": "trims/color_palettes/trim_palette",
                    "permutations": {
                        "quartz": "trims/color_palettes/quartz",
                        "iron": "trims/color_palettes/iron",
                        "gold": "trims/color_palettes/gold",
                        "diamond": "trims/color_palettes/diamond",
                        "netherite": "trims/color_palettes/netherite",
                        "redstone": "trims/color_palettes/redstone",
                        "copper": "trims/color_palettes/copper",
                        "emerald": "trims/color_palettes/emerald",
                        "lapis": "trims/color_palettes/lapis",
                        "amethyst": "trims/color_palettes/amethyst",
                    },
                },
            ]
        }

    # Add the new permutation to the existing data
    data["sources"][-1]["permutations"][item_name] = f"trims/color_palettes/{item_name}"

    # Save the updated JSON back to the file
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

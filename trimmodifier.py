# This is the main() function
from colorPicker import colorPicker
from resources.resourceRecursionAgent import recursiveWrapper
from clean import deleteFolder
from materialGenerator import generate_material

imi = 0.001

while True:
    item = input("Enter the Trim Material: ")
    ingredient = input("Enter the Item ID: ")
    color = colorPicker()
    generate_material(item, ingredient, imi, color)
    print("Material generated successfully!")
    again = input("Do you want to generate another material? (y/n): ")
    if again == "y":
        imi = imi + 0.001
    elif again == "clean":
        deleteFolder("./ingotcraftDataPack")
        deleteFolder("./ingotcraftResourcePack")
        break
    else:
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "turtle_helmet")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "chainmail_helmet")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "gold_helmet")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "iron_helmet")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "diamond_helmet")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "netherite_helmet")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "chainmail_chestplate")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "gold_chestplate")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "iron_chestplate")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "diamond_chestplate")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "netherite_chestplate")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "chainmail_leggings")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "gold_leggings")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "iron_leggings")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "diamond_leggings")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "netherite_leggings")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "chainmail_boots")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "gold_boots")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "iron_boots")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "diamond_boots")
        recursiveWrapper("./ingotcraftResourcePack/assets/minecraft/models/item", "netherite_boots")
        break


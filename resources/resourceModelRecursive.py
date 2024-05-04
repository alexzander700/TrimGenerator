# This file will call resourceRecursionAgent on every trim added.
import os

from CustomTrims.resources.resourceRecursionAgent import recursiveAgent


def recursiveTrim(item_name, imi):
    folder_path = "./ingotcraftResourcePack/assets/minecraft/models/item"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    recursiveAgent(folder_path, item_name, imi, "turtle_helmet", "helmet")
    recursiveAgent(folder_path, item_name, imi, "chainmail_helmet", "helmet")
    recursiveAgent(folder_path, item_name, imi, "gold_helmet", "helmet")
    recursiveAgent(folder_path, item_name, imi, "iron_helmet", "helmet")
    recursiveAgent(folder_path, item_name, imi, "diamond_helmet", "helmet")
    recursiveAgent(folder_path, item_name, imi, "netherite_helmet", "helmet")
    recursiveAgent(folder_path, item_name, imi, "chainmail_chestplate", "chestplate")
    recursiveAgent(folder_path, item_name, imi, "gold_chestplate", "chestplate")
    recursiveAgent(folder_path, item_name, imi, "iron_chestplate", "chestplate")
    recursiveAgent(folder_path, item_name, imi, "diamond_chestplate", "chestplate")
    recursiveAgent(folder_path, item_name, imi, "netherite_chestplate", "chestplate")
    recursiveAgent(folder_path, item_name, imi, "chainmail_leggings", "leggings")
    recursiveAgent(folder_path, item_name, imi, "gold_leggings", "leggings")
    recursiveAgent(folder_path, item_name, imi, "iron_leggings", "leggings")
    recursiveAgent(folder_path, item_name, imi, "diamond_leggings", "leggings")
    recursiveAgent(folder_path, item_name, imi, "netherite_leggings", "leggings")
    recursiveAgent(folder_path, item_name, imi, "chainmail_boots", "boots")
    recursiveAgent(folder_path, item_name, imi, "gold_boots", "boots")
    recursiveAgent(folder_path, item_name, imi, "iron_boots", "boots")
    recursiveAgent(folder_path, item_name, imi, "diamond_boots", "boots")
    recursiveAgent(folder_path, item_name, imi, "netherite_boots", "boots")


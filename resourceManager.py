# This python file will be called via "resourceManager(item_name)"
# The goal of this file is to call all the other python functions used for generating the resource pack cleanly
# It will call "resourceBlocksGen(item_name)" along with other functions, and print to console whenever each step is done
from resources.resourceRecursionAgent import recursiveWrapper
from resources.resourceModelRecursive import recursiveTrim
from resources.resourceAtlasesBlocks import resourceBlocksGen
from resources.resourceAtlasesTrims import resourceTrimsGen

trims = []

def resourceManager(item_name, imi):
    # Call the function that generates the blocks of the resource pack
    resourceBlocksGen(item_name)
    resourceTrimsGen(item_name)
    recursiveTrim(item_name, imi)
    trims.append(item_name)
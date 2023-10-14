# btw
# this program does not take decimal reborn items into account whatsoever
# all calculations are based off of the open-sourced rbxl of the game from Sep. 16, 2019 on GitHub
# (https://github.com/berezaa/minershaven/blob/master/src/ServerScriptService/Main/RebirthHandler.server.lua)

import item_lists
import math

clr = "\n"*1000
print(clr+
"""Miner's Haven Reborn Chance Calculator
by JONALD


"""
)

while True:

    name = input("Item Name: ")

    while not name in item_lists.reborns and not name in item_lists.advanced_reborns:
        print("No item with that name!")
        name = input("Item Name: ")

    life = input("Life Count: ")

    while not life.isnumeric() or int(life) < 1:
        print("You cannot be under life 1!")
        life = input("Life Count: ")
    life = int(life)

    skips = input("Skip Count: ")

    while not skips.isnumeric() or int(skips) < 0 or int(skips) > 20:
        print("Out of bounds 0-20!")
        skips = input("Skip Count: ")
    skips = int(skips)

    final_data = {}

    total = 0 # total number of items in pool

    for item_name in item_lists.reborns:
        item = item_lists.reborns[item_name]
        if item["Life"] > life + skips + 1: continue
        final_data[item_name] = item["Rarity"]
        total += item["Rarity"]

    for item_name in item_lists.advanced_reborns:
        item = item_lists.advanced_reborns[item_name]
        if item["Life"] > life + skips + 1: continue
        new_rarity = math.ceil( item["Rarity"] * ( (skips+1) * 0.5) )
        final_data[item_name] = new_rarity
        total += new_rarity

    if not name in final_data or final_data[name] == 0:
        print(f"{name} is not obtainable at this point.")
        continue

    odds = (final_data[name] / total) * 100
    print(f"The odds of getting a {name} this rebirth is {odds}%.")
    print("\n\n\n")

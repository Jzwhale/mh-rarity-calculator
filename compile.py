# This is just random code for converting wiki source info into a nice little dictionary
# this isn't used in the program itself but maybe someone will find it useful

import re

# sourced from https://minershaven.fandom.com/wiki/Category:Reborn
reborn_data = """
|{{ItemPic|Banana Split Upgrader}}
|[[:Category:Upgrader|Upgrader]]
|0+
|5
|Multiplies ore value by x5.5
|{{ItemPic|Banana Sundae Refiner}}
|-
|{{ItemPic|Nature's Grip}}
|[[:Category:Cell Furnace|Cell Furnace]]
|0+
|15
|Processes ores worth under {{Money|1k}} at x200B value.<br>Processes ores worth over $1k at x200M value.
|{{ItemPic|Gaia's Grasp}}
|-
|{{ItemPic|Quantum Ore Cleaner}}
|[[:Category:Upgrader|Upgrader]]
|0+
|15
|Quadruples (x4) ore value, can upgrade an ore one time only.
|{{ItemPic|Quantum Ore Polisher}}
|-
|{{ItemPic|Massive Diamond Mine}}
|[[:Category:Dropper|Dropper]]
|0+
|15
|Drops a special diamond ore worth {{Money|10M}} every 10 seconds. Ore can be upgraded and still be accepted by a cell furnace.
|{{ItemPic|Massive Diamond Drill}}
|-
|{{ItemPic|Frozen Justice}}
|[[:Category:Furnace|Furnace]]
|0+
|15
|Processes ore at x10 normally.<br>Processes ore at x26 if ore is on fire.
|{{ItemPic|Frozen Peaks}}
|-
|{{ItemPic|Industrial Firecrystal Mine}}
|[[:Category:Industrial Dropper|Industrial Dropper]]
|0+
|15
|A coal-powered mine that drops ore worth {{Money|15M to $1.5B}}. Some ore produced are compatible with cell furnaces.
|{{ItemPic|Industrial Firegem Quarry}}
|-
|{{ItemPic|Sage Redeemer}}
|[[:Category:Furnace|Furnace]]
|0+
|15
|Processes ore by the number of times it has been upgraded divided by 2, with a cap of 50x.
|{{ItemPic|Sage King}}
|-
|{{ItemPic|Pizza Blaster}}
|[[:Category:Upgrader|Upgrader]]
|0+
|15
|Multiplies ore value by x4
|{{ItemPic|Pizza Bombarder}}
|-
|{{ItemPic|Astral Predictor}}
|[[:Category:Upgrader|Upgrader]]
|0+
|15
|Multiplies ore value randomly from ~1.71x to ~5.79x over 2.2 to 7.2 seconds.
|{{ItemPic|Astral Setter}}
|-
|{{ItemPic|Vortex Chamber}}
|[[:Category:Upgrader|Upgrader]]
|0+
|15
|Multiplies ore value by x5
|{{ItemPic|Vortex Singularity}}
|-
|{{ItemPic|Wild Spore}}
|[[:Category:Upgrader|Upgrader]]
|0+
|17
|Multiplies ore value by 5x once while removing negative status effects from ores an unlimited number of times.
|{{ItemPic|Deadly Spore}}
|-
|{{ItemPic|Righteous Will}}
|[[:Category:Infuser|Infuser]]
|5+
|6
|This infuser will grant complete immunity to [[Explosive Infuser]] enemies, a higher chance to survive [[Adowable Guardian]]s, as well as +30 health, +15 speed, and you can jump higher. Increased resistance to Blaster explosions.
|{{ItemPic|Zenith Will}}
|-
|{{ItemPic|Ancient Temple}}
|[[:Category:Upgrader|Upgrader]]
|5+
|7
|<u>If the ore value is</u>:<br>Whole Number: 5x<br>Decimal Number: 3x
|{{ItemPic|Ancient Coliseum}}
|-
|{{ItemPic|Ore Sawmill}}
|[[:Category:Upgrader|Upgrader]]
|5+
|10
|Ores is split in two ore, halving value and size.
|{{ItemPic|Ore Chainsaw}}
|-
|{{ItemPic|The Catalyst}}
|[[:Category:Upgrader|Upgrader]]
|5+
|12
|Quadruples (x4) ore value. Can only be used once.
|{{ItemPic|Saturated Catalyst}}
|-
|{{ItemPic|Azure Refiner}}
|[[:Category:Upgrader|Upgrader]]
|5+
|15
|Quadruples (x4) ore value. Destroys ore with status effects.
|{{ItemPic|Azure Purifier}}
|-
|{{ItemPic|Ore Illuminator}}
|[[:Category:Upgrader|Upgrader]]
|5+
|15
|Multiplies ore value by x7 after 5 seconds but destroys ore if upgraded in that time. Ore is given Illuminati particles during the 5 seconds.
|{{ItemPic|Ore Indoctrinator}}
|-
|{{ItemPic|Flaming Schrodinger}}
|[[:Category:Upgrader|Upgrader]]
|5+
|16
|Randomly multiplies ore value by x2, x2.6, x4, or x6. Can set ore value to - ({{Money|100}}) or add {{Money|100B}} to ore value. Has a chance to fling or destroy ore.
|{{ItemPic|Super Schrodinger}}
|-
|{{ItemPic|Venomshank}}
|[[:Category:Weapon|Weapon Giver]]
|5+
|3
|Dispenses a Venomshank sword, which boosts the player's speed on equip. On critical hit, the victim is poisoned, losing a chunk of health over time after the initial hit and turning them green.
|N/A
|-
|{{ItemPic|Tesla Resetter}}
|[[:Category:Resetting Device|Resetting Device]]
|10+
|18
|Removes all machine tags, including status effects, can only affect ores once.
|{{ItemPic|Tesla Refuter}}
|-
|{{ItemPic|Yunium Mine}}
|[[:Category:Dropper|Dropper]]
|10+
|17
|A mine that spits out ore worth {{Money|25M to $2.5B}} in any direction. Ores from this mine are lighter than ore from other mines, and will receive bonus upgrades from Cannon items.
|{{ItemPic|Yuttrium Mine}}
|-
|{{ItemPic|Big Bad Blaster}}
|[[:Category:Portable Upgrader|Portable Upgrader]]/[[:Category:Blaster|Blaster]]
|10+
|18
|Multiplies ore value by 2.65x with no limit, but has a chance to destroy ores. will set ores on fire unless the ores resilient to fire or put out with spore
|{{ItemPic|Mad Monsterous Melter}}
|-
|{{ItemPic|Mineral Wheel}}
|[[:Category:Upgrader|Upgrader]]
|10+
|17
|Multiplies ore value by x6
|N/A
|-
|{{ItemPic|Clockwork}}
|[[:Category:Fine-Point|Fine-Point]] [[:Category:Upgrader|Upgrader]]
|10+
|8
|Multiplies ore value by x5.<br>Has a very thin upgrade beam.
|{{ItemPic|Grandfather Clockwork}}
|-
|{{ItemPic|Dreamer's Might}}
|[[:Category:Furnace|Furnace]]
|20+
|15
|Subtracts {{Money|1T}} from ore value, then processes ore at x40.
|{{ItemPic|Dreamer's Valor}}
|-
|{{ItemPic|Big Bertha}}
|Beam-Raised [[:Category:Upgrader|Upgrader]]
|20+
|19
|Normally requires an ore cannon, a drop from a hydraulic conveyor, or a drop from a platform to use. Multiplies ore value by x10 (Some mines such as Atomium and Newtonium can drop directly into Big Bertha)
|{{ItemPic|Tsar Bomba}}
|-
|{{ItemPic|Scorpium Mine}}
|[[:Category:Dropper|Dropper]]
|20+
|17
|Initially drops ore worth {{Money|0}}. Every ore after that is worth 1.2 multiplied by the number of seconds the mine is on the base, with a cap of {{Money|69.2B}}. Ore from this mine is immune to poison.
|{{ItemPic|Scorponyte Mine}}
|-
|{{ItemPic|Newtonium Mine}}
|[[:Category:Dropper|Dropper]]
|20+
|18
|Drops an ore worth {{Money|100M to $5B}} every half second. Ores from this mine are dense, resisting knockback. They also will get bonus upgrades from radioactive upgraders.
|{{ItemPic|Newtonium Excavator}}
|-
|{{ItemPic|Dreamer's Fright}}
|[[:Category:Furnace|Furnace]]
|20+
|18
|Randomly processes ore from (-x5)-x45 while slowly depleting your Research Points.
|{{ItemPic|Dreamer's Terror}}
|-
|{{ItemPic|Plasma Scanner}}
|[[:Category:Upgrader|Upgrader]]
|20+
|19
|Multiplies ore value by x6 if they successfully collide with the moving upgrade beam. Can be used with other scanner variants. Attempting to repeat upgrades will destroy the ore.
|N/A
|-
|{{ItemPic|Lightningbolt Refiner}}
|[[:Category:Button|Button-Powered]] [[:Category:Upgrader|Upgrader]]
|20+
|18
|An upgrader that multiplies ore value by 1x-7x. Requires clicks on a button to work. Ore has a chance to be destroyed if used more than twice.
|{{ItemPic|Tempest Refiner}}
|-
|{{ItemPic|Green Tea Latte}}
|[[:Category:Way-Up-High|Way-Up-High]] [[:Category:Upgrader|Upgrader]]
|20+
|10
|Multiplies ore value by 5x
|{{ItemPic|Green Tea Kettle}}
|-
|{{ItemPic|Scorching Heat}}
|[[:Category:Upgrader|Upgrader]]
|20+
|10
|Will upgrade fireproof or flaming ores by x5, but will destroy other ores.
|{{ItemPic|Searing Heat}}
|-
|{{ItemPic|The Fracture}}
|[[:Category:Cell Furnace|Cell Furnace]]
|20+
|4
|Raises ore to the power of 1.12 then multiplies it by x300M. Does not accept upgraded ore.
|{{ItemPic|The Fissure}}
|-
|{{ItemPic|Solar Flare}}
|[[:Category:Furnace|Furnace]]
|50+
|18
|Processes ore at x25 value during the day.<br>Processes ore randomly from x0 to x50 during nighttime.
|{{ItemPic|Solar Eruption}}<hr>{{ItemPic|Lunar Bombardment}}
|-
|{{ItemPic|Atomium Mine}}
|[[:Category:Dropper|Dropper]]
|100+
|12
|Drops one ore every 0.3 seconds, worth {{Money|3.5B to $25B}}. Receives bonus upgrades if the ore is sparkling, but the ore can get destroyed when sparkling.
|{{ItemPic|Atomyke Mine}}
|-
|{{ItemPic|Dark Magic}}
|[[:Category:Remote|Remote-Powered]] [[:Category:Furnace|Furnace]]
|100+
|18
|Normally processes ore at x12 its value. When remotely activated, it processes ore value by x45.
|{{ItemPic|Forbidden Magic}}
|-
|{{ItemPic|Eternal Journey}}
|[[:Category:Furnace|Furnace]]
|100+
|10
|A furnace that needs 1-15 seconds to process a single ore at 100x. Additional ore will be destroyed but still award Research Points.
|{{ItemPic|Eternal Limbo}}
|-
|{{ItemPic|Toxic Waste Disposal}}
|[[:Category:Upgrader|Upgrader]]
|100+
|13
|Multiplies ore value by x3 to x6, applying a radioactive effect on ores. The radiation will cause ores to explode after 6 seconds. Makes ore lighter.
|{{ItemPic|Demon Core}}
|-
|{{ItemPic|Blind Justice}}
|[[:Category:Cell Furnace|Cell Furnace]]
|100+
|7
|Base x700M value, every +1 upgrade counter reduces multiplier by 70M, every -1 upgrade counter increases multiplier by 70M.
|{{ItemPic|Swift Justice}}
|-
|{{ItemPic|Cooling Chamber}}
|[[:Category:Upgrader|Upgrader]]
|100+
|8
|Normally upgrades ore by x7; flaming ores get extinguished and an x11 upgrade. However, over-usage will cause the item to overheat, weakening its multiplier and preventing it from extinguishing fire.<br>Overheating can be prevented by frozen ore.
|{{ItemPic|Turbine Chamber}}
|-
|{{ItemPic|Atlantic Monolith}}
|[[:Category:Upgrader|Upgrader]]
|100+
|10
|Multiplies ore value by x4, turns them blue, and makes them fireproof.
|{{ItemPic|Atlantic Monument}}
|-
|{{ItemPic|Dragonglass Mine}}
|[[:Category:Remote|Remote-Powered]] [[:Category:Dropper|Dropper]]
|100+
|8
|Remote [[:Category:Dropper|Dropper]] in which its ore value will increase depending on how long the remote is activated from {{Money|4B}} - {{Money|10T}}. Three ores are produced each click-- but only one of them is compatible with cell furnaces. Receives bonus upgrades from Blasters.
|{{ItemPic|Draconicglass Mine}}
|-
|{{ItemPic|Gate of Eclipse}}
|[[:Category:Upgrader|Upgrader]]
|100+
|15
|Multiplies ore value by x4 during the day, and x10 during the night.
|{{ItemPic|Final Eclipse Gate}}
|-
|{{ItemPic|Timeless Enhancement}}
|[[:Category:Furnace|Furnace]]
|150+
|7
|Processes depending on how short the ore's lifespan from 30x to 80x.
|{{ItemPic|Temporal Enchantment}}
|-
|{{ItemPic|Ambrosia Fountain}}
|[[:Category:Furnace|Furnace]]
|150+
|7
|Processes ores depending on how long they have existed. Caps at 10 minutes = 110x.
|{{ItemPic|Ambrosia Forest}}
|-
|{{ItemPic|Dreamer's Anguish}}
|[[:Category:Cell Furnace|Cell Furnace]]
|200+
|3
|Processes un-upgraded ore from 10 to 80qd times its value based on how much money you have (similar to [[Noobite Mine]]).
|{{ItemPic|Dreamer's Nightmare}}
|-
|{{ItemPic|Phase Refiner}}
|[[:Category:Upgrader|Upgrader]]
|200+
|7
|Multiplies ore value by x4. Boosts the [[Phase Processor]]'s multiplier.
|{{ItemPic|Phase Bombarder}}
|-
|{{ItemPic|Pilotite Mine}}
|[[:Category:Hydraulic|Hydraulic]] [[:Category:Dropper|Dropper]]
|200+
|13
|The higher this mine is raised into the sky, the more valuable the ore is. This ore is also more resilient to fire, lasting twice as long compared to other ore types.
|{{ItemPic|V-tolite Mine}}
|-
|{{ItemPic|Guardian of the Gate}}
|[[:Category:Furnace|Furnace]]
|250+
|5
|x20 when the owner is is within the base, and x200 when away from the base.
|{{ItemPic|Guardian of the Portal}}
|-
|{{ItemPic|Morning Star}}
|[[:Category:Star|Star]] [[:Category:Upgrader|Upgrader]]
|250+
|14
|Multiplies ore value by 70% up to {{Money|1N}}. Sets ore on fire.
|N/A
|-
|{{ItemPic|Aether Refinery}}
|[[:Category:Furnace|Furnace]]
|300+
|5
|Processes ores at x90. Afterwards, a barrier is set up blocking ore access for 5 seconds. If an ore was upgraded by Aether Schrodinger, this processes ores at x300 instead.
|{{ItemPic|Aethereal Synthesizer}}
|-
|{{ItemPic|Symmetrium Mine}}
|[[:Category:Dropper|Dropper]]
|300+
|10
|Drops 1 ore worth {{Money|500M to $10B}} and cannot produce another until the ore is processed or destroyed. The ore has a self-upgrading flame, but the upgrade stops if flame is removed. Ore is fireproof.
|{{ItemPic|Symmetryte Mine}}
|-
|{{ItemPic|Sakura Garden}}
|[[:Category:Furnace|Furnace]]
|350+
|3
|Processes pure ore at x300. Every ore processed will lower the multiplier by x1. Processing ore with flames will lower the multiplier by x25, down to a minimum of -x144.
|{{ItemPic|Sakura Falls}}
|-
|{{ItemPic|Invasive Cyberlord}}
|[[:Category:Furnace|Furnace]]
|400+
|10
|Processes ore at a base value of x250. If an ore hits one of the three upgrade beams it gets multiplied by x1.25, with a total multiplier of of ~x488.
|{{ItemPic|Breached Motherboard}}
|-
|{{ItemPic|The Sporest}}
|[[:Category:Upgrader|Upgrader]]
|400+
|8
|Multiplies ore value by x8 and poisons them.
|N/A
|-
|{{ItemPic|Nuclear Stronghold}}
|[[:Category:Furnace|Furnace]]
|400+
|7
|Processes ore at a 200x rate. If ore is radioactive, processes at 290x.
|{{ItemPic|Nuclear Castle}}
|-
|{{ItemPic|Phase Processor}}
|[[:Category:Furnace|Furnace]]
|450+
|7
|Processes ore at x90 normally. If an ore has been upgraded by [[Phase Refiner]] or [[Phase Bombarder]], the furnace will be activated and will process every ore from there by x500.
|N/A
|-
|{{ItemPic|Breech Loader}}
|[[:Category:Dropper|Dropper]]
|500+
|8
|Drops 5 ores every second. Ore is worth {{Money|90B to $900B}}. Ore has a chance to randomly duplicate itself.
|{{ItemPic|Dimension Extractor}}
|-
|{{ItemPic|The Abomination}}
|[[:Category:Dropper|Dropper]]
|500+
|8
|Base ore value of {{Money|10M}}<br>When ore from this mine touches ore from another mine, that ore is destroyed and ore from this mine is upgraded by x2. Can only take in 5 ores.
|{{ItemPic|The Daegelart}}
|-
|{{ItemPic|Crystalized System}}
|[[:Category:Upgrader|Upgrader]]
|600+
|12
|Multiplies ore value by x6
|{{ItemPic|Crystallized Engine}}
|-
|{{ItemPic|Fractured Reality}}
|[[:Category:Upgrader|Upgrader]]
|750+
|5
|Upgrader depends on the status effects the ore has; said status effect is also swapped with another effect.
|{{ItemPic|Universal Collapse}}<hr>{{ItemPic|Temporal Armageddon}}
|-
|{{ItemPic|Ore Skillet}}
|[[:Category:Upgrader|Upgrader]]
|753+
|11
|Multiplies ore value by a base of 2x. Each ore dropped onto the frying pan increases the multiplier by 1 up to 10x
|N/A
|-
|{{ItemPic|Gravitational Gearwork}}
|[[:Category:Hydraulic|Hydraulic]] [[:Category:Anti-Gravity|Anti-Gravity]] [[:Category:Upgrader|Upgrader]]
|800+
|13
|Multiplies ore value by x7. Upgrade beam is on the bottom of the item.
|{{ItemPic|Atmospheric Steamwork}}
|-
|{{ItemPic|Shard Park}}
|[[:Category:Upgrader|Upgrader]]
|800+
|9
|Upgrader is dependent on the amount of Shard of Life the user currently has divided by 2, capping out at x10.
|{{ItemPic|Shard City}}
|-
|{{ItemPic|Newtonic Corroder}}
|[[:Category:Upgrader|Upgrader]]
|1,000+
|10
|Multiplies ore value by x7, and poisons ore. Upgrade beam is above item.
|N/A
|-
|{{ItemPic|Red Giant}}
|[[:Category:Star|Star]] [[:Category:Upgrader|Upgrader]]
|1,000+
|14
|Upgrades ores by 70% up to {{Money|1NvD}}. Sets ore on fire.
|{{ItemPic|Neutron Star}}
|-
|{{ItemPic|Skyliner Flux}}
|[[:Category:Hydraulic|Hydraulic]] [[:Category:Upgrader|Upgrader]]
|1,000+
|7
|Vertical-oriented refiner that upgrades ore by x4. Works up to 3 times, for a total of x64.
|{{ItemPic|Heavenly Flux}}
|-
|{{ItemPic|Industrial Scarab}}
|[[:Category:Furnace|Furnace]]
|5,000+
|3
|Processes ore by 7,750x to 9,100x
|N/A
|-
|{{ItemPic|Desert Monument}}
|[[:Category:Raised|Raised]] [[:Category:Upgrader|Upgrader]]
|7,300+
|1
|Multiplies ore value by x13 and renders them immune to negative cash results from Schrodinger items.
|N/A"""

# sourced from https://minershaven.fandom.com/wiki/Category:Advanced_Reborn
advanced_reborn_data = """
|{{ItemPic|Dragon Blaster}}
|[[:Category:Portable Upgrader|Portable Upgrader]]/[[:Category:Blaster|Blaster]]
|500+
|3
|Multiplies ore value by 4x with a 20% chance of explosion and 10% chance of destroying ore. Sets ore on fire.
|{{ItemPic|Hydra Blaster}}
|-
|{{ItemPic|Frigid Dystopia}}
|[[:Category:Upgrader|Upgrader]]
|500+
|3
|Multiplies ore value by 15x, but only if the ore is frozen.
|{{ItemPic|Auroral Metropolis}}
|-
|{{ItemPic|Precursor Furnace}}
|[[:Category:Furnace|Furnace]]
|500+
|3
|Processes ore value by 70x their value normally, but if an ore from the [[Precursor Mine]] is processed, the multiplier raises to 500x.
|N/A
|-
|{{ItemPic|Precursor Mine}}
|[[:Category:Dropper|Dropper]]
|500+
|3
|Drops ore worth between {{Money|1B - $5B}}. If an ore from this mine enters the [[Precursor Furnace]], the furnace will have its multiplier raised.
|N/A
|-
|{{ItemPic|Vampire Spore}}
|[[:Category:Upgrader|Upgrader]]
|500+
|1
|Multiplies ore value by 11x, but applies one negative effect.
|{{ItemPic|Devil's Spore}}
|-
|{{ItemPic|Vulcan's Grasp}}
|[[:Category:Upgrader|Upgrader]]
|500+
|1
|Multiplier increases based on the number of rebirth-related items on base. Cannot be re-used with resetters.
|{{ItemPic|Vulcan's Destiny}}
|-
|{{ItemPic|Stardust Pulsar}}
|[[:Category:Pulsar|Pulsar]] [[:Category:Upgrader|Upgrader]]
|600+
|2
|Multiplies of your ores value by 35x when pulsed, and cannot be re-used, even with resetters.
|N/A
|-
|{{ItemPic|Hades' Palace}}
|[[:Category:Upgrader|Upgrader]]
|666+
|3
|Multiplies ore with upgrade counter 20 or less by 6x. Every upgrade count increases multiplier by 0.3 up to 30x at 100 upgrades.
|{{ItemPic|Brimstone Spires}}
|-
|{{ItemPic|Sword God Shrine}}
|[[:Category:Weapon|Weapon Giver]]
|800+
|1
|Dispenses Darkheart sword.
|{{ItemPic|Lord of Tenebrous}}
|-
|{{ItemPic|Igneous Forge}}
|[[:Category:Furnace|Furnace]]
|1,000+
|3
|Feeds off coal to power its multiplier. Capped at x975.
|{{ItemPic|Tyrant's Forge}}
|-
|{{ItemPic|Virtual Enhancer}}
|[[:Category:Upgrader|Upgrader]]
|1,000+
|3
|Multiplies ores based how far the dropper is from the upgrader, with a cap of x30. If mine of the ore is removed, it will always upgrade by 1x.
|{{ItemPic|Virtual Enchanter}}
|-
|{{ItemPic|Palladium Drill}}
|[[:Category:Dropper|Dropper]]
|1,000+
|2
|Two types of ores are dispensed from this mine. One is bigger orange which drops directly in front of the mine with a value of $100B. The other is smaller blue which scatters like a [[Yunium Mine]] with a value of {{Money|100T}}.
|N/A
|-
|{{ItemPic|Father of Freon}}
|[[:Category:Upgrader|Upgrader]]
|1,000+
|2
|Upgrades ore by 9x and freezes them, removing fire. Bonus effects when used alongside [[Son of Poison]] and [[Spirit of Fire]].
|N/A
|-
|{{ItemPic|Northern Lights}}
|[[:Category:Furnace|Furnace]]
|2,000+
|1
|Feeds off sparkling coal ore to increase its power. Caps at a multiplier of x2000.
|{{ItemPic|Aurora Borealis}}
|-
|{{ItemPic|Arcane Lightning}}
|[[:Category:Button|Button-Powered]] [[:Category:Upgrader|Upgrader]]
|2,000+
|3
|Each button click adds x1 to a multiplier which caps at x51. The multiplier will quickly decline if left inactive for a minute.
|{{ItemPic|Mystical Thunder}}
|-
|{{ItemPic|Black Dwarf}}
|[[:Category:Resetting Device|Resetting Device]]
|2,000+
|3
|Acts as a resetting device, allowing you to re-use most use limited items again, but destroys ores that have been upgraded by a star loop item (the [[Catalyzed Star|Catalyzed Star's]] first upgrade doesn't count). Ores upgraded by the Black Dwarf cannot be upgraded by stars.
|{{ItemPic|Void Star}}
|-
|{{ItemPic|Dreamer's Blight}}
|[[:Category:Furnace|Furnace]]
|2,000+
|2
|Grants bonuses to spore items while gaining bonuses from them. While bonuses are active, furnace power will "decay" until drained completely. Once decayed, all bonuses stop and the furnace does not process ore.
|{{ItemPic|Dreamer's Devastation}}
|-
|{{ItemPic|Big Alberto}}
|[[:Category:Upgrader|Upgrader]]
|2,000+
|3
|Features two upgrade upgrade parts: hexagon-shaped above conveyor multiplies ore value by x25 while bottom by x10. Only one beam can be used.
|{{ItemPic|Castle Bravo}}
|-
|{{ItemPic|Crystal Shrine}}
|[[:Category:Furnace|Furnace]]
|3,000+
|1
|Processes ores at x3000 if unlocked, but requires a specific method to be unlocked first. Ores are processed at x0 if the furnace is locked.
|{{ItemPic|Crystal Altar}}
|-
|{{ItemPic|Son of Poison}}
|[[:Category:Upgrader|Upgrader]]
|3,000+
|2
|Upgrades ore by 12x and poisons them. Bonus effects when used alongside Father of Freon and Spirit of Fire.
|N/A
|-
|{{ItemPic|Spirit of Fire}}
|[[:Category:Upgrader|Upgrader]]
|3,000+
|2
|Upgrades ore by 10x and sets them on fire. Bonus effects when used alongside Father of Freon and Son of Poison.
|N/A
|-
|{{ItemPic|Nova Star}}
|[[:Category:Star|Star]] [[:Category:Upgrader|Upgrader]]
|5,000+
|3
|Multiplies the effectiveness of other stars by x4 for 5 seconds, with the exception of the Blue Supergiant, which is instead buffed by 25x.
|N/A
|-
|{{ItemPic|Apollium Mine}}
|[[:Category:Dropper|Dropper]]
|5,000+
|1
|Produces ore that receives a bonus upgrade from fire, but cannot be extinguished.
|{{ItemPic|Solarium Mine}}
|-
|{{ItemPic|Railgun Cannon}}
|[[:Category:Utility|Cannon]]
|8,000+
|2
|Sets ore on fire (Regardless of immunity) and launches them a far distance.
|N/A
|-
|{{ItemPic|Blue Supergiant}}
|[[:Category:Star|Star]] [[:Category:Upgrader|Upgrader]]
|10,000+
|2
|Multiplies ore value by x3 with a cap of $1NVG. Sets ores on fire.
|N/A
"""

"""
for entry in reborn_data.split("|-"):

    item_name = re.search(r"{{ItemPic.(.+)}}", entry).group(1)
    life_req = int(re.search(r"(\d*,?\d+)\+", entry).group(1).replace(',',''))
    rarity = int(re.search(r"^\|(\d*)$", entry, re.MULTILINE).group(1))
    
    print(f"\"{item_name}\": {{\"Life\": {life_req}, \"Rarity\": {rarity}}},")

for entry in advanced_reborn_data.split("|-"):

    item_name = re.search(r"{{ItemPic.(.+)}}", entry).group(1)
    life_req = int(re.search(r"(\d*,?\d+)\+", entry).group(1).replace(',',''))
    rarity = int(re.search(r"^\|(\d*)$", entry, re.MULTILINE).group(1))
    
    print(f"\"{item_name}\": {{\"Life\": {life_req}, \"Rarity\": {rarity}}},")
"""
import os
import shutil

downloads = "/home/jake/Downloads"
stamping_room = "."
names = [
"Blue Jay",
"Northern Cardinal",
"American Robin",
"American Goldfinch",
"Baltimore Oriole",
"Scarlet Tanager",
"Cedar Waxwing",
"Rose-breasted Grosbeak",
"Red-winged Blackbird",
"Brown Pelican",
"Superb Lyrebird",
"Eastern Spinebill",
"Crimson Rosella",
"Red Wattlebird",
"Australian Raven",
"Pied Oystercatcher",
"Silver Gull",
"Australian Ibis",
"Sarus Crane",
"Secretarybird",
"Orange-headed Thrush",
"Malabar Whistling Thrush",
"Asian Fairy-bluebird",
"Black-naped Monarch",
"Indian Thick-knee",
"Black-breasted Weaver",
"Brown Fish Owl",
"White-bellied Drongo",
"Azure-winged Magpie",
"Sardinian Warbler",
"Golden Eagle",
"Griffon Vulture",
"Sand Martin",
"Red-legged Partridge",
"Himalayan Monal",
"Crested Bunting",
"Blue-throated Bee-eater",
"Golden Pheasant",
]

things = os.listdir(downloads)
things.sort(key = lambda thing: os.path.getmtime(downloads + "/" + thing))
    
for index, thing in enumerate(things):
    bird = names[index]
    new_name = bird.replace(" ", "") + "1.jpg"  
    
    old_path = downloads + "/" + thing
    new_path = stamping_room + "/" + new_name
    
    shutil.move(old_path, new_path)
print("Done")

import random

#list of settlements
settlements = ["Bloomsville", "Kinkade port", "Spruceville", "Farmers rock"]

# events and their stuff
Bloomsville = {
  "nothing happened!" : {
    "desc" : "today is a nice day isn't it?",
    "cost" : {"money" : [0, 0], "iron" : [0, 0], "wood" : [0, 0]},
    "weight" : 60
}

# randomly picking settlement
settlement = random.choice(settlements)

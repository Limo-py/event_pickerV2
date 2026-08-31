import random
import requests
import sys
import io
WEBHOOK_URL = "https://discord.com/api/webhooks/1536032910514196630/2JEuaUME5W6DtbBXxRfKGbjnTg7soBQjrGmwtHeTG39uJ8ww7tekr9m4DeO2IU-BehZp"
old_stdout = sys.stdout
sys.stdout = catched_output = io.StringIO()

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

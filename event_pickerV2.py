import random
import requests
import sys
import io
WEBHOOK_URL = "https://discord.com/api/webhooks/1536032910514196630/2JEuaUME5W6DtbBXxRfKGbjnTg7soBQjrGmwtHeTG39uJ8ww7tekr9m4DeO2IU-BehZp"
old_stdout = sys.stdout
sys.stdout = catched_output = io.StringIO()

# events and their stuff
bloomsville = {
  "nothing happened!" : {
    "desc" : "Today is a nice day isn't it?",
    "cost" : {"money" : [0, 0], "iron" : [0, 0], "steel" : [0, 0], "wood" : [0, 0]},
    "weight" : 20},
  "bridge collapsed" : {
    "desc" : "The bridge has collapsed! We lost one snail who was on it. Rest in peace!",
    "cost" : {"money" : [50, 250], "iron" : [0, 3], "steel" : [0, 2], "wood" : [5, 30]},
    "weight" : 20},
  "mayor drunk" : a {
    "desc" : "Mayor was drunk while operating the ship! Don't worry, he's still alive",
    "cost" : {"money" : [100, 100], "iron" : [0, 1], "steel" : [0, 0], "wood" : [0, 5]},
    "weight" : 30},
  "trading station on fire" : {
    "desc" : "The trading station is on fire! Locals think it was JKI, but no evidence was found",
    "cost" : {"money" : [100, 500], "iron" : [5, 15], "steel" : [1, 5], "wood" : [20, 30]},
    "weight" : 10},
  "tornado visited town" : {
    "desc" : "Tornado went straight through the town and destroyed half of the it!",
    "cost" : {"money" : [500, 2000], "iron" : [10, 30], "steel" : [5, 10], "wood" : [30, 60]},
    "weight" : 5},
  "pirate attack" : {
    "desc" : "Pirates attacked! We managed to defend ourselves, but they still destroyed part of the town!"
    "cost" : {"money" : [75, 350], "iron" : [0, 10], "steel" : [0, 1], "wood" : [0, 20]},
    "weight" : 15}
}

# randomly picking settlement
settlements = [bloomsville]
settlement = random.choice(settlements)

sys.stdout = old_stdout 
final_text = catched_output.getvalue()
data = {"content": f"```\n{final_text}\n```"}
requests.post(WEBHOOK_URL, json=data)

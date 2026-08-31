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
    "desc" : "today is a nice day isn't it?",
    "cost" : {"money" : [0, 0], "iron" : [0, 0], "copper" : [0, 0], "steel" : [0, 0], "wood" : [0, 0]},
    "weight" : 60
}

# randomly picking settlement
settlements = [bloomsville]
settlement = random.choice(settlements)

sys.stdout = old_stdout 
final_text = catched_output.getvalue()
data = {"content": f"```\n{final_text}\n```"}
requests.post(WEBHOOK_URL, json=data)

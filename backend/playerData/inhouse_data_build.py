# Imports #
import requests
import opendota
import json
import pandas as pd

# Variables #
client=opendota.OpenDota()
api_key="4eced22c-924d-4aa3-8a36-d4205ec34cfe"
openURL="https://api.opendota.com/api/"
playersURL="players/"
timID='99084628'

#get requests for data #
playerTim=requests.get(openURL+playersURL+timID)
r = requests.get(playerTim)
data = json.loads(r.text)
df = pd.DataFrame(data)
df.head(10)

#changes#
#t

# Outputs #
print(df)
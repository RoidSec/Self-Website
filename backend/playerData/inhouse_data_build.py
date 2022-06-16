# Imports #
import requests
import opendota
import json
import pandas as pd

# Variables #
client=opendota.OpenDota()
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
# Imports #
import requests
import opendota

# Variables #
client=opendota.OpenDota()
api_key="4eced22c-924d-4aa3-8a36-d4205ec34cfe"
openURL="https://api.opendota.com/api/"
playersURL = "players/"
timID='99084628'
shaunID='145692671'
ivanID='51625083'
harryID='83942876'
anthonyID='282780720'
niseID='337288948'
caseyID='69558459'
colinID='44067861'
connorID='39958451'

playerTim=requests.get(openURL+playersURL+timID)
timData=playerTim.json()
playerShaun=requests.get(openURL+playersURL+shaunID)
shaunData=playerShaun.json()
playerIvan=requests.get(openURL+playersURL+ivanID)
ivanData=playerIvan.json()
playerHarry=requests.get(openURL+playersURL+harryID)
harryData=playerHarry.json()
playerAnthony=requests.get(openURL+playersURL+anthonyID)
anthonyData=playerAnthony.json()
playerNise=requests.get(openURL+playersURL+niseID)
niseData=playerNise.json()
playerCasey=requests.get(openURL+playersURL+caseyID)
caseyData=playerCasey.json()
playerColin=requests.get(openURL+playersURL+colinID)
colinData=playerColin.json()
playerConnor=requests.get(openURL+playersURL+connorID)
connorData=playerConnor.json()

print('Tim MMR -',timData['mmr_estimate'],'Actual:',timData['solo_competitive_rank'])
print()
print('Shaun MMR -',shaunData['mmr_estimate'])
print('')
print('Ivan MMR -',ivanData['mmr_estimate'])
print('')
print('Harry MMR -',harryData['mmr_estimate'])
print('')
print('Anthony MMR -',anthonyData['mmr_estimate'])
print('')
print('Shanise MMR -',niseData['mmr_estimate'])
print('')
print('Casey MMR -',caseyData['mmr_estimate'])
print('')
print('Colin MMR -',colinData['mmr_estimate'])
print('')
print('Connor MMR -',connorData['mmr_estimate'])
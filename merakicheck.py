
from webexteamssdk import WebexTeamsAPI
import requests

meraki_api_key = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
mynetwork = 'L_646829496481100388'

msversion = '11.31'
mrversion = '26.6.1'
mxversion = '15.27'
mvversion = '4.0'
msversion = msversion.replace(".", "-")
mrversion = mrversion.replace(".", "-")
mxversion = mxversion.replace(".", "-")
mvversion = mvversion.replace(".", "-")
i = 0
mscount = 0
mrcount = 0
mxcount = 0
mvcount = 0
checkdeviceserial = []
checkdevicemodel = []

WebexRoomID = "Y2lzY29zcGFyazovL3VzL1JPT00vNWJiMmRiZjAtNmFkOC0xMWVhLWEzNmEtMDc0ZjMxN2Y0Njli"
# MyWebexToken = ""
# you will need to put your personal token here
webexapi = WebexTeamsAPI()    #Using WEBEX_TEAMS_ACCESS_TOKEN variable in PyCharm

baseurl = "https://dashboard.meraki.com/api/v0/networks/"

payload = None
headers = {
    "X-Cisco-Meraki-API-Key": meraki_api_key,
    "Content-Type": "application/json",
    "Accept": "application/json"
} #you will need to look to the meraki_api_key

url = baseurl + mynetwork + '/devices'  #finish the url!

response = requests.request("GET", url, headers=headers, data = payload) #complete the api call using the requests library

myresponse = response.json()

# print(myresponse)

for devices in myresponse:
    if msversion in myresponse[i]['firmware']:
        mscount += 1
    elif mrversion in myresponse[i] ['firmware']:
        mrcount += 1
    elif mxversion in myresponse[i] ['firmware']:
        mxcount += 1
    elif mvversion in myresponse[i] ['firmware']:
        mvcount += 1
    else:
        checkdeviceserial.append(myresponse[i]['serial'])
        checkdevicemodel.append(myresponse[i]['model'])
    i += 1
print('Total switches that meet standard: ' + str(mscount))
print('Total APs that meet standard: ' + str(mrcount))
print('Total Security Appliances that meet standard: ' + str(mxcount))
print('Total Cameras that meet standard: ' + str(mvcount))
print('Devices that will need to be manually checked: ')
for serial,model in zip(checkdeviceserial,checkdevicemodel):
    print('Serial#:', serial, 'Model#:', model)

webexapi.messages.create(WebexRoomID, text="Report Completed")
import requests

import json


url = "https://platform.uipath.com/api/Account/Authenticate"

payload = {"TenancyName":"sriharishtenancy","UsernameOrEmailAddress":"sriharish.gutta@accenture.com","Password":"Harish613"}

response = requests.request("POST", url, data=payload)


responseText = json.loads(response.text)

access_token = responseText['result']



header = {'Content-Type': 'application/json' , 'Authorization' : "Bearer " + access_token}

url = "https://platform.uipath.com/odata/Robots"

response = requests.request("GET", url, headers=header)
responseText = json.loads(response.text)
Robot_id = responseText['Id']

url = "https://platform.uipath.com/odata/Releases"
response = requests.request("GET", url, headers=header)
responseText = json.loads(response.text)
release_key = responseText['Key']

url = "https://platform.uipath.com/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"


header = {'Content-Type': 'application/json' , 'Authorization' : "Bearer " + access_token}


payload = {"startInfo":{"RobotIds":Robot_id,"ReleaseKey":release_key,"Strategy":"Specific","NoOfRobots":0,"Source":"Manual"}}

response = requests.request("POST", url, data=payload, headers=header)

print (response.text)

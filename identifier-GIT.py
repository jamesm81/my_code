import requests
import json
import time

def listPeople(myDisplayName):

	url = "https://api.ciscospark.com/v1/people"

	querystring = {
		#"displayName": "jim matthews"
		"displayName": myDisplayName
		}

	headers = {
	    'content-type': "application/json",
	    'authorization': "Bearer ",
	    #'cache-control': "no-cache",
	    #'postman-token': "30417136-3dd5-9cf7-bb03-3a177327dc55"
	    }

	response = requests.request("GET", url, headers=headers, params=querystring)
	#response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
	#response = requests.request("GET", url, data=json.dumps(querystring), headers=headers)
	
	print("ACCESS GRANTED - your spark ID is: ", response.text)
	#print (json.dumps(response,indent=4))
	return response

myDisplayName = input("What is your first and lastname?: ")

listPeople(myDisplayName)
# end def identifier function

while (1)
	response = listPeople()
	peopleData = response["items"]
	for whatsMyID in peopleData:
		id = whatsMyID

	print ("your id is:",id)

import requests
import json
import time

##Spark API call to send a message to the roomId.
def sparkCall(mymsg):
	url = "https://api.ciscospark.com/v1/messages"

	#payload = "{\n\t\"roomId\": \"Y2lzY29zcGFyazovL3VzL1JPT00vMjE0ODYwNTAtZjZkMC0xMWU1LThmOWYtYmQ5ZjQ4OTI3OGZh\",\n\t\"text\": \"Hi John\"\n}"
	payload  = {
		"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNTI5Mzg3YjAtNjU1My0xMWU2LTllNTItMDE0YzYwYmM3NWZk",
		"text": mymsg
	}
	headers = {
	    'content-type': "application/json",
	    'authorization': "Bearer x",
	    }


	response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

## showCommand function.  Takes a show command and returns the results
def showCommand(mycmd):
	url='http://198.18.134.17/ins'
	switchuser='admin'
	switchpassword='Cisco321'

	myheaders={'content-type':'application/json'}
	payload={
	  "ins_api": {
	    "version": "1.0",
	    "type": "cli_show",
	    "chunk": "0",
	    "sid": "1",
	    "input": mycmd,
	    "output_format": "json"
	  }
	}
	response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

	print (json.dumps(response,indent=4))
	return response
## end def showCommand(mycmd): function

cmd = "show ip int brief"

while(1):
	response= showCommand(cmd)
	interfaceData = response["ins_api"]["outputs"]["output"]["body"]["TABLE_intf"]
	for showInterfaceInfo in interfaceData:
		interfaceName = showInterfaceInfo["ROW_intf"]["intf-name"]
		interfaceIP = showInterfaceInfo["ROW_intf"]["prefix"]
		interfacelinkState = showInterfaceInfo["ROW_intf"]["link-state"]
		interfaceAdminState = showInterfaceInfo["ROW_intf"]["admin-state"]
		interfaceProtocolState = showInterfaceInfo["ROW_intf"]["proto-state"]
		if (interfaceName == 'Eth1/9'):
			if (interfacelinkState == 'down'):
				sparkCall("Rolly, Eth 1/9 is down, please fix")			

	print ("my interface name is:",interfaceName)
	print ("my ip is:",interfaceIP)
	print ("my link state is:",interfacelinkState)
	print ("my admin state is:", interfaceAdminState)
	print ("my protocol state is:", interfaceProtocolState)

	time.sleep(10)




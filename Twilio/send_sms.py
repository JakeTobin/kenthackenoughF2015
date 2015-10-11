from twilio.rest import TwilioRestClient
from random import randint
import time

# Accound SID and Authentication token
account_sid = "ACbd52b365826fece7a22bfc14995e0b1a"
auth_token  = "cd946105ffc78ef8341d40a633dcb09d"
client = TwilioRestClient(account_sid, auth_token)

#send poll
partiers = ["+16142035285", "+17244949644","+14404872954","+13308089943",]

partyPlaces = ["Patty's Pub","The World's End", "Yer Mum's Place",]

placesStr = ""
for i in range(len(partyPlaces)):
	placesStr += "%s. %s \n" %(i+1,partyPlaces[i])

placesStr = "Yo it's party time! Where should we go?\n" + placesStr

for peeps in partiers:
	message = client.messages.create(to=peeps, from_="+17245082021",
                                     body=placesStr)

#Makes a list of SMSs
SMS = client.sms.messages.list(To="+17245082021")

def deleteSms(smsList):
	tmp = []
	for i in smsList:
		tmp.append(i.sid)
		print i.sid

	for i in tmp:
		client.messages.delete(i)
	print len(smsList)
deleteSms(SMS)

#Wait for partier response
time.sleep(10)

#Get updated SMS list
SMS = client.sms.messages.list(To="+17245082021")


votes = [0,0,0]

for i in range(0, len(SMS)):

	print SMS[i].body
	votes[int(SMS[i].body)-1] += 1
	print votes

destination = "We're going to: " + partyPlaces[votes.index(max(votes))]

for peeps in partiers:
	message = client.messages.create(to=peeps, from_="+17245082021",
                                     body=destination)
from twilio.rest import TwilioRestClient
import datetime 
import time

# Accound SID and Authentication token
account_sid = "ACbd52b365826fece7a22bfc14995e0b1a"
auth_token  = "cd946105ffc78ef8341d40a633dcb09d"
client = TwilioRestClient(account_sid, auth_token)

#send poll
partiers = ["+16142035285", "+17244949644","+14404872954",]

for peeps in partiers:
	message = client.messages.create(to=peeps, from_="+17245082021",
                                     body="\n\nYo it's party time! Where should we go?\n1. Patty's Pub\n2. The World's End\n3. Yer mums place\n4. I'm lame and can't go")

#Makes a list of SMSs
SMS = client.sms.messages.list(To="+17245082021")

#Only necessary to see what is being retrieved
#for i in range (0, len(SMS)):
#	print SMS[i].body
#print "\n"

#Store length of old message list before overwriting
qtyOld = len(SMS)	

#Wait for partier response
time.sleep(20)

#Get updated SMS list
SMS = client.sms.messages.list(To="+17245082021")
#Get the number of new SMSs
quantity = len(SMS) - qtyOld

votes = [0,0,0]

for i in range(0, quantity):
	print SMS[i].body
	if(SMS[i].body == '1'):
		votes[0] += 1
		print 'added\n'
	if(SMS[i].body == '2'):
		votes[1] += 1
		print 'added\n'
	if(SMS[i].body == '3'):
		votes[2] += 1
		print 'added\n'
#Kent Hack Enough Fall 2015
#The Party Button
#Wes Delp, Lawerence Kelly, Ben Warner, Jake Tobin
#10.11.2015

import subprocess
import time
import os
import signal
import requests
import json
from twilio.rest import TwilioRestClient
from random import randint

#MUSIC FUNCTIONALITY
def playMusic():
	musicProcess = subprocess.Popen("mplayer 'partySong.mp3'", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
	print "Music Started!"
	return(musicProcess)

def killMusic(musicProcess):
	os.killpg(musicProcess.pid, signal.SIGTERM) 
	print "Music Stopped!"

#UBER FUNCTIONALITY
def testUberProducts():
	url = 'https://api.uber.com/v1/products'

	parameters = {
		'server_token': 'z3eHieu-BbrsHBa3NgpD9_jAhRhta-VeXO-IMKhv',
		'latitude': 41.1465470,
		'longitude': -81.3425080,
	}
	response = requests.get(url, params=parameters)
	data = response.json()
	
	for product in range(0,2):
		print data['products'][product]['description']
		print "Capcity:", data['products'][product]['capacity']
		print "Cost per minute:", data['products'][product]['price_details']['cost_per_minute'],"\n"

#TWILIO FUNCTIONALITY
class TwilioAuth():
	def __init__(self):
		self.account_sid = "ACbd52b365826fece7a22bfc14995e0b1a"
		self.auth_token  = "cd946105ffc78ef8341d40a633dcb09d"
		self.client = TwilioRestClient(self.account_sid, self.auth_token)
		self.partiers = ["+16142035285", "+17244949644","+14404872954","+13308089943",]
		self.partyPlaces = ["Patty's Pub","The World's End", "Yer Mum's Place",]

def clearMessages():
	auth = TwilioAuth()
	account_sid = auth.account_sid
	auth_token  = auth.auth_token
	client = auth.client
	
	SMS = client.sms.messages.list(To="+17245082021")
	tmp = []
	for i in SMS:
		tmp.append(i.sid)
	for i in tmp:
		client.messages.delete(i)

def sendTextPoll():
	clearMessages()
	
	auth = TwilioAuth()
	account_sid = auth.account_sid
	auth_token  = auth.auth_token
	client = auth.client
	
	placesStr = ""
	for i in range(len(auth.partyPlaces)):
		placesStr += "%s. %s \n" %(i+1,auth.partyPlaces[i])
	placesStr = "Yo it's party time! Where should we go?\n" + placesStr

	for peeps in auth.partiers:
		message = client.messages.create(to=peeps, from_="+17245082021",
	                                     body=placesStr)
	print "Sent Poll!"

def getTextPoll():
	auth = TwilioAuth()
	account_sid = auth.account_sid
	auth_token  = auth.auth_token
	client = auth.client
	
	SMS = client.sms.messages.list(To="+17245082021")
	votes = [0,0,0]

	for i in range(0, len(SMS)):
		print SMS[i].body
		votes[int(SMS[i].body)-1] += 1
		print votes

	destination = "We're going to: " + auth.partyPlaces[votes.index(max(votes))]

	for peeps in auth.partiers:
		message = client.messages.create(to=peeps, from_="+17245082021", 
		                                body=destination)
	print "Sent Results"

sendTextPoll()
time.sleep(15)
getTextPoll()
testUberProducts()




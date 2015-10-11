#Kent Hack Enough Fall 2015
#The Party Button
#Wes Delp, Lawerence Kelly, Ben Warner, Jake Tobin
#10.11.2015

import subprocess
import time
import os
import signal
import requests
import httplib, urllib
import json
import time
from twilio.rest import TwilioRestClient
from random import randint

from flask import Flask, flash, redirect, render_template, request, url_for
import logging

from logging.handlers import RotatingFileHandler

app = Flask(__name__)

partyTime = 30

#MUSIC FUNCTIONALITY
def playMusic():
	musicProcess = subprocess.Popen("mplayer 'partySong.mp3'", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
	print "Music Started!"
	return(musicProcess)

def killMusic(musicProcess):
	os.killpg(musicProcess.pid, signal.SIGTERM)
	print "Music Stopped!"

#UBER FUNCTIONALITY
def testUber(location):
	url = 'https://api.uber.com/v1/products'

	parameters = {
		'server_token': 'z3eHieu-BbrsHBa3NgpD9_jAhRhta-VeXO-IMKhv',
		'latitude': 41.1465470,
		'longitude': -81.3425080,
	}
	response = requests.get(url, params=parameters)
	data = response.json()

	print "AVAILABLE UBER SERVICES IN YOUR AREA:"
	print "UBER X",data['products'][0]['description']
	print "Capcity:", data['products'][0]['capacity']
	print "Cost per minute:", data['products'][0]['price_details']['cost_per_minute']
	print "UBER schduled to go to",location,"- Enjoy the ride!"

#TWILIO FUNCTIONALITY
class TwilioAuth():
	def __init__(self):
		self.account_sid = "ACbd52b365826fece7a22bfc14995e0b1a"
		self.auth_token  = "cd946105ffc78ef8341d40a633dcb09d"
		self.client = TwilioRestClient(self.account_sid, self.auth_token)
		self.partiers = ["+16142035285", "+17244949644","+14404872954","+13308089943",]
		self.partyPlaces = ["Paddy's Pub","The World's End", "Yer Mum's Place",]

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
		votes[int(SMS[i].body)-1] += 1

	destination = "We're going to: " + auth.partyPlaces[votes.index(max(votes))]

	for peeps in auth.partiers:
		message = client.messages.create(to=peeps, from_="+17245082021",
		                                body=destination)
	print "Sent Results"
	return auth.partyPlaces[votes.index(max(votes))]

#PEBBLE AND WATCH FUNCTIONALITY
def notifyWatches(message):
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
		urllib.urlencode({
			"token": "awinwWShGff3mMgtcS2AL6eACEaBRF",
			"user": "uKQwc95wPBWVXnBuzWRk1NQy1DA7DY",
			"message": message,
		}), { "Content-type": "application/x-www-form-urlencoded" })
	conn.getresponse()
	print "Watch notified with code"


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/button1', methods=['POST'])
def add_entry():
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    sendTextPoll()
    notifyWatches("Let the party begin!")
    music = playMusic()

    time.sleep(partyTime)

    notifyWatches("Time to leave!")
    location = getTextPoll()
    testUber(location)
    killMusic(music)
    return "1"

@app.route('/button2', methods=['POST'])
def add_entry2():
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    playMusic()
    return "2"

@app.route('/button3', methods=['POST'])
def add_entry3():
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    testUber("Paddy's Pub")
    return "3"

@app.route('/button4', methods=['POST'])
def add_entry4():
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    sendTextPoll()
    time.sleep(partyTime)
    getTextPoll()
    return "4"

if __name__ == '__main__':
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0')
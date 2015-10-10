#!/usr/bin/python

import requests
from rauth import OAuth2Service

uber_api = OAuth2Service(
	client_id='Bnn2CPk9w89wHHL1ZKeky24glmtNEOfG',
	client_secret='SP97CyVnF-_poch_6ey0_i9HT_GFM1jAAKJYe4o1',
	name='thePartyButton',
	authorize_url='https://login.uber.com/oauth/authorize',
	access_token_url='https://login.uber.com/oauth/token',
	base_url='https://api.uber.com/v1/',
)

parameters = {
	'response_type': 'code',
	'redirect_uri': 'INSERT_ROUTE_TO_STEP_TWO',
	'scope': 'profile',
}

# Redirect user here to authorize your application
login_url = uber_api.get_authorize_url(**parameters)

parameters = {
	'redirect_uri': 'INSERT_ROUTE_TO_STEP_TWO',
	'code': request.args.get('code'),
	'grant_type': 'authorization_code',
}

response = requests.post(
	'https://login.uber.com/oauth/token',
	auth=(
		'INSERT_CLIENT_ID',
		'INSERT_CLIENT_SECRET',
	),
	data=parameters,
)

# This access_token is what we'll use to make requests in the following
# steps
access_token = response.json().get('access_token')






url = 'https://api.uber.com/v1/products'

parameters = {
	'server_token': 'INSERT_SERVER_TOKEN_HERE',
	'latitude': 37.775818,
	'longitude': -122.418028,
}

response = requests.get(url, params=parameters)

data = response.json()

print data
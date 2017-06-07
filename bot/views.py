from django.shortcuts import render
from django.http import HttpResponse
import json
import random
import requests
import sys
sys.path.append('/home/sansuke05/prog/python/LINEbot/sora/bot/')
from loads_dic import dic

# debuglog
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

# Create your views here.

def index(request):
	return HttpResponse("This is bot api.")

# Constants
REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = 'uj50mDTxG1fW3f59zXUO67NFdwurWYzpM12mhNzlNvX9kuXd/5xJo1X0rPX3ZdmRhiwb/BFKppP0A8P1hjvLijfsGVWgEehqLvynzCx/E4S6/sOjza5fGm7KbwF7msq9CCP8tY0C25CEfYHhUf27GwdB04t89/1O/w1cDnyilFU='
HEADER = {
	"Content-Type": "application/json",
	"Authorization": "Bearer " + ACCESS_TOKEN
}

# Functions
def callback(request):
	reply = ""
	request_json = json.loads(request.body.decode('utf-8'))
	for e in request_json['events']:
		reply_token = e['replyToken']
		message_type = e['message']['type']
		logger.debug('request json: ' + json.dumps(e))

		if message_type == 'text':
			text = e['message']['text']
			reply += reply_text(reply_token, text)
	return HttpResponse(reply)

def reply_text(reply_token, text):
	reply = random.choice(dic)
	url = "https://linechatbotsora.herokuapp.com/img/sample.jpg"
	payload = {
		"replyToken":reply_token,
		"messages":[
			{
				"type":"text",
				"text": reply
			},
			{
				"type":"image",
				"originalContentUrl": url,
				"previewImageUrl": url
			}
		]
	}

	logger.debug('reply json:' + json.dumps(payload))
	requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload))
	return reply
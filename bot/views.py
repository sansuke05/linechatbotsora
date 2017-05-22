from django.shortcuts import render
from django.http import HttpResponse
import json
import random
import requests
import sys
sys.path.append('/home/sansuke05/prog/python/LINEbot/sora/bot/')
from loads_dic import dic

# Create your views here.

# def index(request):
#    return HttpResponse("This is bot api.")

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = ''
HEADER = {
	"Content-Type": "application/json",
	"Authorization": "Bearer " + ACCESS_TOKEN
}


def callback(request):
	reply = ""
	request_json = json.loads(request.body.decode('utf-8'))
	for e in request_json['events']:
		reply_token = e['replyToken']
		message_type = e['message']['type']

		if message_type == 'text':
			text = e['message']['text']
			reply += reply_text(reply_token, text)
	return HttpResponse(reply)

def reply_text(reply_token, text):
	reply = random.choice(dic)
	payload = {
		"replyToken":reply_token,
		"message":[
			{
				"type":"text",
				"text": reply
			}
		]
	}

	requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload))
	return reply
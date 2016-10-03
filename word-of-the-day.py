from wordnik import *
import json
import datetime
import urllib

def func():
	now=datetime.datetime.now()
	today=str(now.year)+'-'+str(now.month)+'-'+str(now.day)
	url='http://api.wordnik.com:80/v4/words.json/wordOfTheDay?date='+today+'&api_key=d52b63b6880f17811310d0fbd3b0d3a8ef163a248f58dc831'
	response=urllib.urlopen(url)
	word=json.load(response)
	x=word['word']
	word_of_the_day=bytes(x)
	y=word['note']
	note=bytes(y)
	meaning=word['definitions'][0]['text']
	print "*****************************************"
	print "The word of the day is: "+word_of_the_day
	print "Meaning: "+meaning
	print "Note : "+note
	print "*****************************************"

func()

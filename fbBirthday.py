import urllib.request,json.requests
from bs4 import BeautifulSoup

request=urllib.request.urlopen("https://graph.facebook.com/me/posts?access_token={access_token}")
a=request.read()
req=request.json()

msg_id_array=[]
for msg in req['data']['msg']:
	if(msg['message']=="Happy Birthday"):
	    msg_id_array.append(msg['id'])	
	
for i in msg_array:
	current_id=i
	payload={'access_token':'acc_tok',message:'Thank you'}	
    post_reg=req.post("https://graph.facebook.com/me/posts"+current_id+"/"+params=payload)
	
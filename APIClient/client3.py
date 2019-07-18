import requests, sys, time

text_len = 0

def getUrl(text, session):
  url = 'http://turnincode.cafe24.com:8880/home/sessions/'+session+'/stones/'
  res = requests.get(url)
  if res.status_code == 404:
    time.sleep(1)
    getUrl(session)
  if (text == len(res.text)):
    time.sleep(1)
    getUrl(session)
  else:
    text_len = len(res.text)

if sys.argv[2] == 'b':
  data = {'room': sys.argv[1], 'color': 'black', 'x1' : 'A', 'y1' : 6 , 'x2' : '', 'y2' : 0}
  res = requests.post('http://turnincode.cafe24.com:8880/home/sessions/'+sys.argv[1]+'/stones/', data=data)
  getUrl(text_len, sys.argv[1])
  data = {'room': sys.argv[1], 'color': 'black', 'x1' : 'B', 'y1' : 5 , 'x2' : 'C', 'y2' : 4}
  res = requests.post('http://turnincode.cafe24.com:8880/home/sessions/'+sys.argv[1]+'/stones/', data=data)
  getUrl(text_len, sys.argv[1])
  data = {'room': sys.argv[1], 'color': 'black', 'x1' : 'D', 'y1' : 3 , 'x2' : 'E', 'y2' : 2}
  res = requests.post('http://turnincode.cafe24.com:8880/home/sessions/'+sys.argv[1]+'/stones/', data=data)
  getUrl(text_len, sys.argv[1])
  data = {'room': sys.argv[1], 'color': 'black', 'x1' : 'F', 'y1' : 1 , 'x2' : 'F', 'y2' : 2}
  res = requests.post('http://turnincode.cafe24.com:8880/home/sessions/'+sys.argv[1]+'/stones/', data=data)

if sys.argv[2] == 'w':
  getUrl(text_len, sys.argv[1])
  time.sleep(1)
  data = {'room': sys.argv[1], 'color': 'white', 'x1' : 'A', 'y1' : 6 , 'x2' : 'B', 'y2' : 5}
  res = requests.post('http://turnincode.cafe24.com:8880/home/sessions/'+sys.argv[1]+'/stones/', data=data)
  getUrl(text_len, sys.argv[1])
  data = {'room': sys.argv[1], 'color': 'white', 'x1' : 'C', 'y1' : 4 , 'x2' : 'D', 'y2' : 3}
  res = requests.post('http://turnincode.cafe24.com:8880/home/sessions/'+sys.argv[1]+'/stones/', data=data)
  getUrl(text_len, sys.argv[1])
  data = {'room': sys.argv[1], 'color': 'white', 'x1' : 'E', 'y1' : 2 , 'x2' : 'F', 'y2' : 1}
  res = requests.post('http://turnincode.cafe24.com:8880/home/sessions/'+sys.argv[1]+'/stones/', data=data)
  getUrl(text_len, sys.argv[1])



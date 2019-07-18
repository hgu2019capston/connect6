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
  data = {'room': sys.argv[1] , 'color': 'black', 'x1' : 'J', 'y1' : 10, 'x2' : '', 'y2' : 0}
  res = requests.post('http://turnincode.cafe24.com:8880/home/sessions/'+sys.argv[1]+'/stones/', data=data)
  getUrl(text_len, sys.argv[1])
  
  number = [5, 7, 9]
  for i in number:
      time.sleep(1)
      if i == 9:
        data = {'room': sys.argv[1], 'color': 'black', 'x1' : 'J', 'y1' : i , 'x2' : 'J', 'y2' : i+4}
      else :
        data = {'room': sys.argv[1], 'color': 'black', 'x1' : 'J', 'y1' : i , 'x2' : 'J', 'y2' : i+1}
      res = requests.post('http://turnincode.cafe24.com:8880/home/sessions/'+sys.argv[1]+'/stones/', data=data)
      getUrl(text_len, sys.argv[1])

if sys.argv[2] == 'w':
  getUrl(text_len, sys.argv[1])
  number = [5, 7, 9]
  for i in number :
      time.sleep(1)
      data = {'room': sys.argv[1], 'color': 'white', 'x1' : 'I', 'y1' : i , 'x2' : 'I', 'y2' : i+1}
      res = requests.post('http://turnincode.cafe24.com:8880/home/sessions/'+sys.argv[1]+'/stones/', data=data)
      getUrl(text_len, sys.argv[1])



import requests, sys, time

url = 'http://turnincode.cafe24.com:8880/api/sessions/'+sys.argv[1]+'/stones/'
 
if sys.argv[2] == 'b':
  data = {'room': sys.argv[1] , 'color': 'black', 'x1' : 'D', 'y1' : 10, 'x2' : '', 'y2' : 0}
  requests.post(url, data=data)
  time.sleep(1)
  requests.get(url)
  data = {'room': sys.argv[1] , 'color': 'white', 'x1' : 'E', 'y1' : 10, 'x2' : 'E', 'y2' : 11 }
  requests.post(url, data=data)
  time.sleep(2)
  requests.get(url)
  data = {'room': sys.argv[1] , 'color': 'black', 'x1' : 'F', 'y1' : 13, 'x2' : 'F', 'y2' : 16 }
  requests.post(url,data=data)
  time.sleep(1)
  requests.get(url)
  data = {'room': sys.argv[1] , 'color': 'white', 'x1' : 'E', 'y1' : 12, 'x2' : 'E', 'y2' : 13 }
  requests.post(url, data=data)
  time.sleep(2)
  requests.get(url)
  data = {'room': sys.argv[1] , 'color': 'black', 'x1' : 'J', 'y1' : 15, 'x2' : 'J', 'y2' : 16 }
  requests.post(url, data=data)
  time.sleep(1)
  requests.get(url)
  data = {'room': sys.argv[1] , 'color': 'white', 'x1' : 'E', 'y1' : 14, 'x2' : 'E', 'y2' : 15 }
  requests.post(url, data=data)
  time.sleep(2)
  requests.get(url)
  
 
if sys.argv[2] == 'w':
  data = {'room': sys.argv[1] , 'color': 'white', 'x1' : 'D', 'y1' : 10, 'x2' : '', 'y2' : 0}
  requests.post(url, data=data)
  time.sleep(2)
  requests.get(url)
  data = {'room': sys.argv[1] , 'color': 'black', 'x1' : 'E', 'y1' : 10, 'x2' : 'E', 'y2' : 11 }
  requests.post(url, data=data)
  time.sleep(2)
  requests.get(url)
  data = {'room': sys.argv[1] , 'color': 'white', 'x1' : 'F', 'y1' : 13, 'x2' : 'F', 'y2' : 16 }
  requests.post(url,data=data)
  time.sleep(2)
  requests.get(url)
  data = {'room': sys.argv[1] , 'color': 'black', 'x1' : 'E', 'y1' : 12, 'x2' : 'E', 'y2' : 13 }
  requests.post(url, data=data)
  time.sleep(2)
  requests.get(url)
  data = {'room': sys.argv[1] , 'color': 'white', 'x1' : 'J', 'y1' : 15, 'x2' : 'J', 'y2' : 16 }
  requests.post(url, data=data)
  time.sleep(2)
  requests.get(url)
  data = {'room': sys.argv[1] , 'color': 'black', 'x1' : 'E', 'y1' : 14, 'x2' : 'E', 'y2' : 15 }
  requests.post(url, data=data)
  time.sleep(2)
  requests.get(url)
  
  

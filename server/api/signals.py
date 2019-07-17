from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from .serializers import *
import requests, time, random

@receiver(post_save, sender = Stone)
def stone_post_save(sender, **kwargs):
            tmp = Stone.objects.last()
            resultRoom = Session.objects.get(session_name=tmp.room).id
            resultColor = str(tmp.color)
            resultX1 = str(tmp.x1)
            resultY1 = tmp.y1
            resultX2 = str(tmp.x2)
            resultY2 = tmp.y2

            resultOmok = ResultOmok(room=resultRoom, color = resultColor, x = resultX1 , y = resultY1)
            resultOmok.save()

            resultOmok = ResultOmok(room=resultRoom, color = resultColor, x = resultX2 , y = resultY2)
            resultOmok.save()

	
            clientColor = Session.objects.get(id=resultRoom).color

            if(str(Stone.objects.last().color) == clientColor):
              if(clientColor == "white"):
                  mColor = "black"
              else:
                  mColor = "white"

              time.sleep(2)
              x1 = random.choice('ABCDEFGHIJKLMNOPQRS')
              x2 = random.choice('ABCDEFGHIJKLMNOPQRS')

              y1 = random.randrange(1,20)
              y2 = random.randrange(1,20)

              data = {'room':resultRoom, 'color': mColor , 'x1': x1, 'y1': y1, 'x2': x2, 'y2' : y2}
              requests.post('http://turnincode.cafe24.com:9999/home/sessions/'+str(resultRoom)+'/stones/', data=data)



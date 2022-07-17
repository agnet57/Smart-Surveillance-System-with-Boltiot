# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:10:53 2022

@author: HP
"""
import json
from time import sleep
from boltiot import Bolt
from Face_Recog import recog 
from message import send_msg
from detect_face_video import pr
d=1
api_key="91a27806-4174-4001-9d24-b42a37a3a513"
device_id="BOLT5778783"
mybolt=Bolt(api_key,device_id)
response=mybolt.analogRead('A0')
res=json.loads(response)
#print(res['value'])
#print(type(res))
if int(res['value'])>-1:
    r=mybolt.digitalRead('0')
    t=json.loads(r)
    print(t['value'])
    if d==1:
        o=recog(True)
        if o==1:
           res1=mybolt.digitalWrite('1','HIGH') 
           sleep(1)
           res1=mybolt.digitalWrite('1','LOW')
           send_msg()
    if int(t['value'])==0:
        print(" intruder is there")
        sleep(1)
        res1=mybolt.digitalWrite('1','HIGH') 
        sleep(1)
        res1=mybolt.digitalWrite('1','LOW')
        #send_msg()
        pr()
else:
    print("no one in the room")

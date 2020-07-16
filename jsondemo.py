import json
import smtplib
import sys
import os
import math
import datetime



data = '{"username" : "nilesh" , "password" :"nilesh"}'
jsonData = json.loads(data)
print(jsonData["username"])
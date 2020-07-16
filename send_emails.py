from smtplib import SMTP
from email.mime.text import MIMEText
import hashlib

mail = SMTP(host="mail.vinsys.com", port=587)
mail.starttls() #this will enable one way ssl
mail.login('iot@vinsys.com', 'Vinsys@2019')
fp = open(file="d:/mimedemo.txt", mode='rt', encoding='UTF-8')
mime_msg = MIMEText(fp.read())
fp.close()
mime_msg['Subject'] = "This is Sample Mime Subject"
mime_msg['From'] = 'iot@vinsys.com'
mime_msg['To'] = 'nilesh.devdas@vinsys.com'
mail.sendmail('iot@vinsys.com', 'nilesh.devdas@vinsys.com', mime_msg.as_string())

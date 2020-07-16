from  smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

msg = MIMEMultipart()
msg['Subject'] = "Find Partnership Logos"
msg['From'] = 'iot@vinsys.com'
msg['To'] = 'Nilesh.devdas@vinsys.com'
fp = open('D:/myimages/logo.png' , 'rb')
img = MIMEImage(fp.read())
msg.attach(img)
mail = SMTP(host="mail.vinsys.com", port=587)
mail.starttls() #this will enable one way ssl
mail.login('iot@vinsys.com', 'Vinsys@2019')
mail.sendmail('iot@vinsys.com', 'nilesh.devdas@vinsys.com', msg.as_string())

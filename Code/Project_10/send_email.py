#Project 10 - Send Email
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#replace the next 3 lines with your credentials
from_email_addr = 'YOUR_EMAIL@gmail.com'
from_email_password = 'YOUR_EMAIL_PASSWORD'
to_email_addr = 'TO_YOUR_OTHER_EMAIL@gmail.com'

#set your email message
body = 'Motion was detected in your room'
msg = MIMEText(body)

#set send and recipient
msg['From'] = from_email_addr
msg['To'] = to_email_addr

#set your email subject
msg['Subject'] = 'WARNING'

#connecting to server and sending email
#edit the following line with your provider's SMTP server details
server = smtplib.SMTP('smtp.gmail.com', 587)
#comment out the next line if your email provider doesn't use TLS
server.starttls()
server.login(from_email_addr, from_email_password)
server.sendmail(from_email_addr, to_email_addr, msg.as_string())
server.quit()
print('Email Sent')

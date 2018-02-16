#Project 10 - Intruder Alarm With Email Notifications
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

#import necessary packages
from gpiozero import LED, Button, MotionSensor
import smtplib
from email.mime.text import MIMEText
from signal import pause

#create objects to refer to each LED, the button, and the PIR sensorled_status = LED(17)
led_triggered = LED(18)
button = Button(2)
pir = MotionSensor(4)

#control variables
motion_sensor_status = False
email_sent = False

#arm or disarm the PIR sensor
def arm_motion_sensor():
    global email_sent
    global motion_sensor_status
    if motion_sensor_status == True:
        motion_sensor_status = False
        led_status.off()
        led_triggered.off()
    else:
        motion_sensor_status = True
        email_sent = False
        led_status.on()

#send email when motion is detected and the PIR sensor is armed
def send_email():
    global email_sent
    global motion_sensor_status
    if(motion_sensor_status == True and email_sent == False):
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

        #connect to server and send email
        #edit this line with your provider's SMTP server details
        server = smtplib.SMTP('smtp.gmail.com', 587)
        #comment out this line if your provider doesn't use TLS
        server.starttls()
        server.login(from_email_addr, from_email_password)
        server.sendmail(from_email_addr, to_email_addr, msg.as_string())
        server.quit()
        email_sent = True
        led_triggered.on()
        print('Email Sent')

#assign a function that runs when the button is pressed
button.when_pressed = arm_motion_sensor
#assign a function that runs when motion is detected
pir.when_motion = send_email

pause()

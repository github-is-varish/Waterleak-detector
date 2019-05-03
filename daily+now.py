


A = 1
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)
pin = 16
import time
from time import sleep
GPIO.setup(pin, GPIO.IN)
status = GPIO.input(pin)
print ('GPIO pin status', status)
print ('A is', A)

while A == 1:
    print ('in while loop')
    status = GPIO.input(pin)
    print ('GPIO pin status', status)
    B = 1
    while status:
        status = GPIO.input(pin)
        print ('GPIO pin status', status)
        B = B + 1
        print ('B is', B)
        print ('before if loop')
        #GPIO.cleanup
        if B == 10:
            # used to circumvent false alarms caused by fluctuations
            print ('in if loop')
            print ('B is:', B)
            print('there is elec')
            status = GPIO.input(pin)
            print ('GPIO pin status', status)
            #Send text msg
            from twilio.rest import Client
            account_sid ="ACc8c6d113f0a69299a25a38d7cb3d138c"
            auth_token ="d1868568633dd5466dc96671976c0831"
            client = Client(account_sid, auth_token)
            message = client.api.account.messages.create(
            to="+12032249872",
            from_="+12039418973",
            body="ALERT!!! A LEAK YOU BETTER COME TO THE LEAK SITE")
            #start mail
            #A = False
            #B = False
            #break
            import smtplib
            content="ALERT!!! THERE IS A LEAK!!!!!"
            sender='varishduriseti@gmail.com'
            recipient='varishduriset@gmail.com'
            mail=smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo() #identify computer
            mail.starttls() # transport layer security
            mail.login('varishduriseti@gmail.com', 'varish06897')
            header = 'To:' + recipient + '\n' + 'From: ' + sender  + '\n ' + 'Subject:water leak \n'
            content=header+content
            mail.sendmail(sender,recipient,content)
            mail.quit()
            # end mail
            A = False 
            B = 0
            print ("reset B to 0")
            print (B)
            time.sleep(10)
    #86400
    else:
        #A = 0
        print('there is no elec')
        time.sleep(6)

    #print ('A is ', A)
print ('exited while loop')
print ('A is final', A)
GPIO.cleanup





            # 



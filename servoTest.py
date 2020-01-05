import math
import smtplib
import RPi.GPIO as GPIO
import time


def mail():
 gmail_user = 'sybilappas@gmail.com'
 gmail_password = 'jutgbudcssqagjyw'

 sent_from = gmail_user
 to = ['anatole.dupre@gmail.com', 'sybilappas@gmail.com']
 subject = 'OMG Super Important Message'
 body = 'Hey, whats up?\n\n- Connect you to this web page see your children : 192.168.137.81/BABYPHONE.php '

 email_text = """\
 From: %s
 To: %s
 Subject: %s
 %s
 """ % (sent_from, ", ".join(to), subject, body)

 try:
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.ehlo()
  server.login(gmail_user, gmail_password)
  server.sendmail(sent_from, to, email_text)
  server.close()
  print('Email sent!')
 except Exception as e:
  print('Something went wrong...')
  print(str(e))
def angle_to_percent (angle) :
 #Set function to calculate percent from angle
  if angle > 180 or angle < 0 :
   return False

  start = 4
  end = 12.5
  ratio = (end - start)/180 #Calcul ratio from angle to percent

  angle_as_percent = angle * ratio

  return start + angle_as_percent
def servoon():

 #!/usr/bin/env python3
 #-- coding: utf-8 -- 

 GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
 GPIO.setwarnings(False) #Disable warnings

 #Use pin 12 for PWM signal
 pwm_gpio = 12
 frequence = 50
 GPIO.setup(pwm_gpio, GPIO.OUT)
 pwm = GPIO.PWM(pwm_gpio, frequence)

 for i in range(1,2) :

  #Init at 0
  pwm.start(angle_to_percent(0))
  time.sleep(1)

  #Go at 90
  pwm.ChangeDutyCycle(angle_to_percent(90))
  time.sleep(1)

  #Finish at 180
  pwm.ChangeDutyCycle(angle_to_percent(180))
  time.sleep(1)

  #Close GPIO & cleanup
 #pwm.stop()
 #GPIO.cleanup()
def servooff():
 #!/usr/bin/env python3
 #-- coding: utf-8 --
 #Close GPIO & cleanup
 GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
 GPIO.setwarnings(False) #Disable warnings
 #Close GPIO & cleanup
 pwm_gpio = 12
 frequence = 50
 GPIO.setup(pwm_gpio, GPIO.OUT)
 pwm = GPIO.PWM(pwm_gpio, frequence)
 pwm.stop()
 GPIO.cleanup()
 

def bangbang():
  
  fichier= open("/home/pi/lireecrire.txt","r")  
  contenu = 0
  contenustr = fichier.read()
 
  if len(contenustr)>0:
   contenu= int(contenustr)
  if( contenu == 1) :
   servoon()
   mail()
  if( contenu == 0):
   servooff()
  fichier.close()

def main():

 while 1:
  bangbang()

main()



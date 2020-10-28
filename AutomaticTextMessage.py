# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import schedule, random, time
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number
from text_quotes import Motivational_Messages

#!API to send the preset messages via text
def send_WakeUpText(quotes_list = Motivational_Messages):
  account_sid = twilio_account
  auth_token = twilio_token
  client = Client(account_sid, auth_token)
  quote = quotes_list[random.randint(0, len(quotes_list) - 1)] #Selects a random quote from the quote list

  message = client.messages.create(body=quote,from_=twilio_number, to=cellphone) #creates and send message to the number
  print("")
  print(message.sid) #message send key
  print("")
  print(message.body) #prints the message contents so you can see what it says


  
  
  
  
  
#*Wakeup Text
schedule.every().day.at("05:00").do(send_WakeUpText)#Sends text every day at 5AM

#*MidDay Text
schedule.every().day.at("14:00").do(send_WakeUpText)#Sends text every day at 2pm

#*Nightly Text
schedule.every().day.at("21:00").do(send_WakeUpText)#Sends text every day at 9pm

while True:
  #checks whether a schedule task is pending to run or not
  schedule.run_pending()
  time.sleep(2) 

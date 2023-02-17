import pywhatkit as pwk
import datetime
# using Exception Handling to avoid unexpected errors
try:
     
     # i = 0      
     # for i in range(50):
        pwk.sendwhatmsg("//enter a number with country code", "hiiiiiiii", datetime.datetime.now().hour,datetime.datetime.now().minute+1)
        print("Message Sent!") #Prints success message in console
 
 
     # error message
except: 
     print("Error in sending the message")
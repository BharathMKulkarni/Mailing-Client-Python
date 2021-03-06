# ESSENTIAL IMPORTS
from email import message
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

# STARTING A SERVER
server = smtplib.SMTP_SSL("smtp.gmail.com")

# READING THE PASSWORD:
with open("password.txt","r") as file:
    pwd = file.read()

# LOGGING INTO THE GMAIL ACCOUNT FIRST:
emailID = "bharathmkulkarni@gmail.com"
server.login(emailID,pwd)

# COMPOSING THE MESSAGE HEADER:
msg = MIMEMultipart('alternative')

receiverEmailID = "dummy@gmail.com"
msg['From'] = emailID
msg['To'] = receiverEmailID

msg['Subject'] = "Test Email-Sorry for the Spam :)"

# COMPSOING THE MESSAGE BODY:
with open("content.txt","r") as file:
    content = file.read()

msg.attach(MIMEText(content, 'plain'))
text = msg.as_string()

# FINALLY SENDING THE EMAIL
server.sendmail(emailID,receiverEmailID,text)

# STOPPING THE SERVER
server.quit()





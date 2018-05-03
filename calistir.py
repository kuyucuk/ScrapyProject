import os
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
#subprocess.check_output(['ls','-l']) #all that is technically needed...

os.system("scrapy crawl sneakerslinkler")
os.system("scrapy crawl sneakers")
os.system("python scrapyproject\spiders\wordchanger.py")
os.system("dataX.xml")
os.system("del database.db")


text="Güncel Sneakers verileri alındı!"
sendMail="tolga_k94@hotmail.com"
file = str("dataX.xml")
recipients = [sendMail]
emaillist = [elem.strip().split(',') for elem in recipients]

msg = MIMEMultipart()
msg['Subject'] = str(file)
msg['From'] = 'usertolga@gmail.com'
msg['Reply-to'] = sendMail
msg.preamble = 'Multipart massage.\n'

part = MIMEText(text)
msg.attach(part)

part = MIMEApplication(open(file, "rb").read())
part.add_header('Content-Disposition', 'attachment', filename=file)
msg.attach(part)

server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("usertolga@gmail.com", "gmailsifresi")

server.sendmail(msg['From'], emaillist, msg.as_string())

print("Mail gönderilmiştir")

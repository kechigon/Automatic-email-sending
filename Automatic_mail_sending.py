import csv
from email.mime.text import MIMEText
import re
import smtplib

def create_message(text, lst):
	res = text
	for i in range(1, len(lst)):
		res = re.sub('<<' + str(i) + '>>', lst[i], res)
	return res
 
account = input("sender gmail address:")
password = input("password:")

subject = input("mail title:")

csv_path = input("path to csv:")
text_path = input("path to template text:")
 
from_email = account

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(account, password)

with open(csv_path) as c:
	reader = csv.reader(c)
	send_list = [row for row in reader]

with open(text_path) as t:
	text = t.read()

for s in send_list:
	to_email = s[0]

	message = create_message(text, s)
	msg = MIMEText(message, "html")
	msg["Subject"] = subject
	msg["To"] = to_email
	msg["From"] = from_email

	server.send_message(msg)

server.quit()
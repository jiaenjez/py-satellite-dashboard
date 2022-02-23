import email.message
import smtplib

msg = email.message.EmailMessage()

sender = input("sender email")
receiver =input("receiver email")

msg["From"] = sender
msg["To"] = receiver
msg["Subject"]="[CubeSat] Satellite passed notification"

# # send original text
# msg.set_content("")

"""
Add if-statement to test whether the satellite pass thru UCI
"""

# send w html
msg.add_alternative("<h2>Test email</h2>This is the test email from python program", subtype="html")

account=input("sender account: ")
password=input("password: ")

# connect to SMTP server
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login(account,password)
server.send_message(msg)

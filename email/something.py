import smtplib
from decouple import config

SMTP_PASS = config("SMTP_PASS")
GOOGLE_SMTP = config("GOOGLE_SMTP")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")

sent_from = EMAIL_HOST
to = ['medsabdulgbenga@gmail.com', 'peacefanifosi2@gmail.com']
subject = 'Python class'
body = "Hi How are you doing?"

email_text = """
From: {}
To: {}
Subject: {}

{}
""".format(sent_from, ", ".join(to), subject, body)

server = smtplib.SMTP_SSL(GOOGLE_SMTP, EMAIL_PORT)
server.ehlo()

server.login(EMAIL_HOST, SMTP_PASS)

server.sendmail(EMAIL_HOST, to, email_text)

server.quit()
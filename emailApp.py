from email.message import EmailMessage 

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
import smtplib

email_sender = 'lilyriddlegranger@mail.com'
email_password = 'xzzyfmvfnjlygtuc'


email_receiver = 'ilef.boualleeg@gmail.com'
subject = "Study hard"
body = """
    You must work hard to be proud of yourself 
    and make your goals a reality!
    Keep going Ilef! You're so close!
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
print(em)
context = ssl.create_default_context()


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
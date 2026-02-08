import smtplib
import os
import datetime as dt
import random

def send_email(content, recipient):
    sender_email='john_deere@gmail.com'
    my_password=os.environ['PWD_EMAIL']
    
    with smtplib.SMTP('smtp.gmail.com:587') as connection:
        connection.starttls()
        connection.login(user=sender_email, password=my_password)
        connection.sendmail(from_addr=sender_email, to_addrs=recipient, msg=f'Subject:Happy birthday\n\n{content}')

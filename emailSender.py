import smtplib, ssl
from decouple import config

port = config("EMAIL_PORT")  # For SSL


def sendEmail(sender, password, receiver, message):
    mail = smtplib.SMTP('smtp.gmail.com',port)
    mail.ehlo()
    mail.starttls()
    mail.login(sender,password)
    mail.sendmail(sender,receiver, message)
    mail.close()    

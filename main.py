#import lib to connect to the server

import smtplib

to= input("Enter the email of the recipent:\n")

content = input("Enter the content for mail:\n")

def sendEmail(to,content):
    server =smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('vemulashivani2002@gmail.com','vemulasurya@2012')
    server.sendmail('vemulashivani2002@gmail.com', to , content)
    server.close()

sendEmail(to, content)
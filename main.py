from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

app = Flask(__name__)


def send_test_mail(body):
    sender_email = "ENTER YOUR NAME"                                 #display name to show who sent the email 
    test = ["Enter Emails HERE","@something.com"]                    #enter emails in a list
    for items in test:
        receiver_email = items

        msg = MIMEMultipart()
        msg['Subject'] = 'TEST MAIL'
        msg['From'] = sender_email
        msg['To'] = receiver_email

        msgText = MIMEText('<b>%s</b>' % (body), 'html')
        msg.attach(msgText)
                                                                    #enter file names here
        pdf = MIMEApplication(open("ENTER FILENAME HERE.pdf", 'rb').read())
        pdf.add_header('Content-Disposition', 'attachment', filename="ENTER FILENAME HERE.pdf")
        msg.attach(pdf)
                                                                    
        pdf2 = MIMEApplication(open("ENTER FILENAME HERE.pdf", 'rb').read())
        pdf2.add_header('Content-Disposition', 'attachment',
                        filename="ENTER FILENAME HERE.pdf")
        msg.attach(pdf2)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login("YOUR_EMAIL@gmail.com", "YOUR PASS")         #enter email and password
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
        print("done with", items)


@app.route('/')
def hello_world():
    return "Hello world!"


if __name__ == "__main__":
    send_test_mail('''
EMAIL BODYY
        ''')
    app.run('0.0.0.0', port=5000)

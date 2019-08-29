import smtplib
from email.message import EmailMessage

emailObject = smtplib.SMTP_SSL('smtp.googlemail.com',465)
emailObject.ehlo()
#emailObject.starttls()
emailObject.login('YourEmail@gmail.com', 'YourPassword')
message = EmailMessage()
message.set_content('body of email!')
message['Subject'] = 'This a subject!'
message['From'] = 'YourEmail@gmail.com'
message['To'] = 'YourRecipient@gmail.com'
try:
    emailObject.send_message(message)
    print("sent")
    #This is deprecated, feel free to use if you dont want to include a subject or anything
    # 
    #
    #emailObject.sendmail('YourEmail@gmail.com', 'YourRecipient@gmail.com', 'Just a test body!')

except:
    print (fail)


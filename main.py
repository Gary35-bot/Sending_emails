import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = 'gafrica851@gmail.com'
receiver_email = 'gafrica851@gmail.com, thapelo@lifechoices.co.za'
password = input("Enter your password: ")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

message = "hey it me "
message = message + "How is work today?"
msg.attach(MIMEText(message, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(sender_email, password)

s.sendmail(sender_email, receiver_email, text)
s.quit()

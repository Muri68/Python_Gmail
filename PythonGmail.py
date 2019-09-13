import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = input("Please enter your Email Address: \n")
receiver_email = input("Please enter reciever Email Address: \n")
password = input(str("Please enter your Email Password: \n"))
subject = input("Please enter Email Subject: \n")

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject


body = input("Typr your Message: ")
message.attach(MIMEText(body,'plain'))
text = message.as_string()

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.starttls()
mail.login(sender_email, password)
print("Login Successfuly")

mail.sendmail(sender_email, receiver_email, text)
print("Email Sent to", receiver_email)
mail.quit()

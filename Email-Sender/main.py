import smtplib
import datetime as dt
import random

quotes = []
with open("Email-Sender/quotes.txt", "r") as file:
    for line in file:
        quotes.append(line.strip())

def send_quote():
    my_email = "tjanssen4@gmail.com"
    my_password = "uyvz rzlt qbbv pdjo"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="timothyjanssen4@gmail.com", msg=f"Subject:Motivation\n\n{random.choice(quotes)}")
        # connection.close() Not needed if using with keyword
        print("Message Sent!!!!")

now = dt.datetime.now()
year = now.year
if now.weekday() == 5:
    send_quote()
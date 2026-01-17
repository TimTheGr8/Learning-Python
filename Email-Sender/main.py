import smtplib
import datetime as dt
import random

MY_EMAIL = "tjanssen4@gmail.com"
MY_PASSWORD = "uyvz rzlt qbbv pdjo"
quotes = []

def get_quotes():
    global quotes
    with open("Email-Sender/quotes.txt", "r") as file:
        for line in file:
            quotes.append(line.strip())

def send_quote():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="timothyjanssen4@gmail.com", msg=f"Subject:Motivation\n\n{random.choice(quotes)}")
        # connection.close() Not needed if using with keyword
        print("Message Sent!!!!")

now = dt.datetime.now()
year = now.year
if now.weekday() == 5:
    send_quote()
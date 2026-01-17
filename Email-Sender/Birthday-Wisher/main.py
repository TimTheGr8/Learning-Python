##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import datetime as dt
import random
# ----- VARIABLES ----- #
MY_EMAIL = "tjanssen4@gmail.com"
MY_PASSWORD = "uyvz rzlt qbbv pdjo"

# ---------------------------- CHOOSE RANDOM LETTER ------------------------------- #
def choose_letter():
    letter_number = random.randint(1, 10)
    
# ---------------------------- CHOOSE RANDOM LETTER ------------------------------- #

# ---------------------------- CHOOSE RANDOM LETTER ------------------------------- #

# ---------------------------- CHOOSE RANDOM LETTER ------------------------------- #


# -----  ----- #
now = dt.datetime.now()
# day = now.day
# month = now.month
data = pd.read_csv("Email-Sender/Birthday-Wisher/birthdays.csv")
birthday_list = data.to_dict(orient="records")
print(birthday_list)
for index in range(len(birthday_list)):
    person = birthday_list[index]
    day = person["day"]
    month = person["month"]
    if day == now.day:
        print(person["name"])

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
def send_quote():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="timothyjanssen4@gmail.com", msg=f"Subject:Motivation\n\n{random.choice(quotes)}")
        # connection.close() Not needed if using with keyword
        print("Message Sent!!!!")

# now = dt.datetime.now()
# year = now.year
# if now.weekday() == 5:
#     send_quote()  Email-Sender\Birthday-Wisher\birthdays.csv
import smtplib
import datetime as dt
import random

MY_EMAIL = "pedramos21@gmail.com"
PASSWORD = "uduydvahokqlcdnx"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

        with smtplib.LMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=MY_EMAIL, 
                msg=f"Subject:Monday Motivation\n\n{quote}"
                )
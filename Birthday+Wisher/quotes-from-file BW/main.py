# import smtplib
# my_email = $$$$
# password = $$$$
#
# with  smtplib.SMTP("smtp.gmail.com") as connection:
#     # securing the connection
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="", msg="Subject:Hello\n\n This is the body of my email")
#
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# print(type(now))
#
# date_of_birth = dt.datetime(year=, month=, day=, hour=4)
# print(date_of_birth)

import datetime as dt
import random
import smtplib
import os

# getting the day of the week
now = dt.datetime.now()
day_of_week = now.weekday()

# reading qutes.txt
with open("quotes.txt") as quotes:
    quotes_list = quotes.readlines()

# picking the random string
random_quote = random.choice(quotes_list)

# sending an email
if day_of_week == 6:
    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("PASSWORD_SMTPLIB")
    to_email = os.getenv("TO_EMAIL")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email,
                            msg=f"Subject:Hello, darling!\n\n {random_quote}")

import smtplib
import datetime as dt
import random
import pandas
import os

my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD_SMTPLIB")
to_email = os.getenv("TO_EMAIL")

now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month, today_day)

birthdays_data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in birthdays_data.iterrows()}
print(birthdays_dict[(5,2)]['name'])

if (today_month, today_day) in birthdays_dict:
    n = random.randint(1, 3)
    with open(f"letter_templates/letter_{n}.txt") as letter_file:
        letter = letter_file.read()
        letter_to = letter.replace("[NAME]", birthdays_dict[(today_month, today_day)]['name'])
        print(letter_to)
    

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email,
                            msg=f"Subject:Hello, darling!\n\n {letter_to}")



##################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

from main_email_sending import connection

now = dt.datetime.now()
today = (now.month, now.day)
# another way to do this: today = (dt.datetime.now().month, dt.datetime.now().day)

my_email = "sujbert1997@gmail.com"
my_password = "something"

data = pandas.read_csv('birthdays.csv')

birthday_dict = {(data_row.month,data_row.day) : data_row for (index, data_row) in data.iterrows()}
print(birthday_dict)
#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    recipient_email = birthday_person["email"]
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=recipient_email,
                        msg=f"Subject:Happy Birthday!\n\n{contents}")
    connection.close()

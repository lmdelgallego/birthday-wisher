from datetime import datetime
import smtplib
import pandas
import random

USR = "alucardluis@hotmail.com"
PWD = "password"

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {
    (data_row.get("month"), data_row.get("day")): data_row for (index, data_row) in data.iterrows()
}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, 'r') as file:
        content = file.read()
        new_content = content.replace("[NAME]", birthday_person.get('name'))

    with smtplib.SMTP(host="smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USR, password=PWD)
        connection.sendmail(
            from_addr=USR,
            to_addrs=birthday_person.get('email'),
            msg=f"Subject: Happy Birthday!\n\n{new_content}"
        )

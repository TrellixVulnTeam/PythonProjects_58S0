import smtplib
import datetime as dt
import random
MY_EMAIL = "plantasticnature@gmail.com"
PASSWORD = "anaaremere1234567890"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="vid.barbaro@gmail.com",
                            msg=f"Subject:Friday Motivation\n\n{quote}"
                            )

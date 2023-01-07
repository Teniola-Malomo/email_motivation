import datetime as dt
import random
import smtplib


now = dt.datetime.now()
day_of_the_week = now.weekday()


with open("quotes.txt") as file:
    all_quotes = file.readlines()
    random_quote = random.choice(all_quotes)


with open("devotional.txt", encoding='utf8') as file:
    bible_passages = file.readlines()
    random_bible_quote = random.choice(bible_passages)
    i = 0
    while not random_bible_quote[i].isalpha():
        i += 1
    bible_quote = random_bible_quote[i - 1:]
    print(bible_quote.replace('—', ""))


port = 465
my_email = "chopchip623@gmail.com"
my_password = "ceqghnhxxxkcgeeb"
receiver_emails = ["teniola.tm@gmail.com", "malomoteniola630@mgmail.com", "teni2002@yahoo.com",
                   "teniola.malomo2@mail.dcu.ie", "emmanuelolumidemalomo@gmail.com", "Damolamalomo9@gmail.com",
                   "adeolamalomo@yahoo.ie", "malomo321music@gmail.com"]
message = f"Subject:Monday Motivation (Python Project)\n\n{random_quote}"
bible_passage = f"Subject:Monday Bible Message (Python Project)\n\n{bible_quote}"

if day_of_the_week == 0:
    for receiver_email in receiver_emails:
        server = smtplib.SMTP_SSL("smtp.gmail.com", port)
        server.login(my_email, my_password)
        server.sendmail(my_email, [receiver_email], message)


if day_of_the_week == 6:
    for receiver_email in receiver_emails:
        server2 = smtplib.SMTP_SSL("smtp.gmail.com", port)
        server2.login(my_email, my_password)
        server2.sendmail(my_email, [receiver_email], bible_passage.encode())
        server2.quit()

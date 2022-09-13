from datetime import datetime
from os import getenv
import schedule
import tweepy
import time

from dotenv import load_dotenv

load_dotenv()
APIKEY = getenv("APIKEY")
SECRET_KEY = getenv("SECRET_KEY")
BEARER = getenv("BEARER")
TOKEN = getenv("TOKEN")
TOKEN_SECRET = getenv("TOKEN_SECRET")

auth = tweepy.OAuthHandler(APIKEY, SECRET_KEY)
auth.set_access_token(TOKEN, TOKEN_SECRET)
client = tweepy.Client(bearer_token=BEARER, consumer_key=APIKEY, consumer_secret=SECRET_KEY, access_token=TOKEN,
                       access_token_secret=TOKEN_SECRET, wait_on_rate_limit=True)
xenobladeDate = datetime.strptime("29/07/22", '%d/%m/%y')
zeldaDate = datetime.strptime("12/05/23", "%d/%m/%y")


def xenoblade_timer():
    if datetime.now() > xenobladeDate:
        client.create_tweet(text="IT'S FUCKING OUT NOW!! #XenobladeChronicles3")
    else:
        timeLeft = xenobladeDate - datetime.now()
        days = timeLeft.days
        seconds = timeLeft.seconds
        leftString = f"{days} days"
        if seconds > 60:
            minutes = int(timeLeft.seconds / 60)
            seconds = seconds % 60
            leftString = f" {minutes} minutes and {seconds} seconds"
            if minutes > 60:
                hours = int(minutes / 60)
                minutes = minutes % 60
                leftString = f"{hours} hours {minutes} minutes and {seconds} seconds"
        texto = f"{leftString} until #XenobladeChronicles3"
        client.create_tweet(text=texto)


def xenoblade_timer2():
    if datetime.now() > xenobladeDate:
        client.create_tweet(text="YA ESTÁ PUTO DISPONIBLE!! #XenobladeChronicles3")
    else:
        timeLeft = xenobladeDate - datetime.now()
        days = timeLeft.days
        seconds = timeLeft.seconds
        leftString = f"{days} días"
        if seconds > 60:
            minutes = int(timeLeft.seconds / 60)
            seconds = seconds % 60
            leftString = f"{minutes} minutos y {seconds} segundos"
            if minutes > 60:
                hours = int(minutes / 60)
                minutes = minutes % 60
                leftString = f"{hours} horas {minutes} minutos y {seconds} segundos"
        texto = f"{leftString} hasta #XenobladeChronicles3"
        client.create_tweet(text=texto)


def zelda_timer():
    if datetime.now() > zeldaDate:
        client.create_tweet(text="IT'S FUCKING OUT NOW!! #TheLegendOfZelda")
    else:
        timeLeft = zeldaDate - datetime.now()
        days = timeLeft.days
        seconds = timeLeft.seconds
        leftString = f"{days} days"
        if seconds > 60:
            minutes = int(timeLeft.seconds / 60)
            seconds = seconds % 60
            leftString = f" {minutes} minutes and {seconds} seconds"
            if minutes > 60:
                hours = int(minutes / 60)
                minutes = minutes % 60
                leftString = f"{days} days {hours} hours {minutes} minutes and {seconds} seconds"
        texto = f"{leftString} until #TheLegendOfZelda Tears of The Kingdom"
        client.create_tweet(text=texto)


def zelda_timer2():
    if datetime.now() > zeldaDate:
        client.create_tweet(text="YA ESTÁ PUTO DISPONIBLE!! #TheLegendOfZelda Tears of The Kingdom")
    else:
        timeLeft = zeldaDate - datetime.now()
        days = timeLeft.days
        seconds = timeLeft.seconds
        leftString = f"{days} días"
        if seconds > 60:
            minutes = int(timeLeft.seconds / 60)
            seconds = seconds % 60
            leftString = f"{minutes} minutos y {seconds} segundos"
            if minutes > 60:
                hours = int(minutes / 60)
                minutes = minutes % 60
                leftString = f"{days} días {hours} horas {minutes} minutos y {seconds} segundos"
        texto = f"{leftString} hasta #TheLegendOfZelda Tears of The Kingdom"
        client.create_tweet(text=texto)


def main():
    zelda_timer()
    time.sleep(5)
    zelda_timer2()
    schedule.every(2).hours.do(zelda_timer2)
    time.sleep(5)
    schedule.every(2).hours.do(zelda_timer)

    while True:
        try:
            schedule.run_pending()
            time.sleep(15)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

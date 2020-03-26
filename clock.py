import requests

from settings import WAIT_KEYBOARD
from viberbot.api.messages import TextMessage
from app import  Session, User, viber
import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    session = Session()
    users = session.query(User)
    for u in users:
        if datetime.datetime.utcnow() >= u.time_reminder:
            viber.send_messages(u.viber_id, [TextMessage(text="Время повторить слова", keyboard=WAIT_KEYBOARD,
                                                         tracking_data='tracking_data')])

@sched.scheduled_job('interval', minutes=10)
def wake_up():
    r = requests.get('https://lastbotpro.herokuapp.com/')

sched.start()

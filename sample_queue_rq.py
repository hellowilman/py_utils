__author__ = 'wilman'
# this script is a demo for using the sample queue system base on redis

# step one: install redis and run it in backgroud

# step two: start the worker ( the worker should be start in the same folder of the project,
# so that it can import the package of the project currently

# step three: add the task to the queue (please install Redis Queue first (python-rq.org, pip install rq)

from sendemail import GmailSendEmail
from rq import Queue
from redis import Redis
from test_case import job_task


# create a queue
q = Queue(connection = Redis())

result = q.enqueue(job_task,{"email":'zwilman@gmail.com',"name":'w.w. zou','msg':'What a day 11'})
result = q.enqueue(job_task,{"email":'zwilman@gmail.com',"name":'w.w. zou','msg':'What a day 21'})
result = q.enqueue(job_task,{"email":'zwilman@gmail.com',"name":'w.w. zou','msg':'What a day 31'})
result = q.enqueue(job_task,{"email":'zwilman@gmail.com',"name":'w.w. zou','msg':'What a day 41'})







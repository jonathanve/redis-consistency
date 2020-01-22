# -*- coding: utf-8 -*-
import time
import redis

from datetime import datetime
from threading import Timer

# redis conn
r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# vars
N = 50
KEY = 'count:ff'
MEMBERS = list(range(1, N + 1))
print('total members:', N)

def incr_count():
    print(datetime.now().ctime(), 'incr global count')
    r.setnx(KEY, 0)
    val = r.get(KEY)
    new_val = int(val) + 1
    r.set(KEY, new_val)

# Jobs
def count_job(numbers):
    print("# Count Job Started:", datetime.now().ctime())
    for n in numbers:
        incr_count()
        time.sleep(0.1)

# start jobs from next minute
now = datetime.now()
delay = 60 - now.second
Timer(delay, count_job, args=[MEMBERS]).start()

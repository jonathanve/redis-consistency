# -*- coding: utf-8 -*-
import time
import redis

from datetime import datetime
from threading import Timer

# redis conn
r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# vars
N = 50
KEY = 'count:sc'
MEMBERS = list(range(1, N + 1))
print('total members:', N)

# register lua script
lua_script = """
redis.call('SETNX', KEYS[1], 0)
local value = redis.call('GET', KEYS[1])
value = tonumber(value)
local new_value = value + 1
redis.call('SET', KEYS[1], new_value)
return new_value
"""
increment = r.register_script(lua_script)

def incr_count():
    print(datetime.now().ctime(), 'incr global count')
    increment(keys=[KEY], args=[])

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

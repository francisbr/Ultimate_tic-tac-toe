import atexit
from time import time
from datetime import timedelta
import decimal

# def secondsToStr(t):
#     return str(timedelta(seconds=t))

line = "="*40
def log(s, elapsed=None):
    if elapsed:
        print(line)
        elapsed = decimal.Decimal(elapsed)
        print("Time:", round(elapsed,3), "second(s)")
        print(line)
        print()

def endlog():
    end = time()
    elapsed = end-start
    log("End Program", (elapsed))

def now():
    return (time())

start = time()
atexit.register(endlog)
log("Start Program")
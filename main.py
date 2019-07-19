import datetime
import time
import os
def process():
    print(f"Hello {datetime.datetime.now()}", flush=True)

print("mypass = " + os.getenv('mypass', "notfound"))
print("mongoConnectionString = " + os.getenv('mongoConnectionString', "notfound"))

while True:
    process()
    time.sleep(20)



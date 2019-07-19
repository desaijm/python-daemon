import datetime
import time
import os
def process():
    print(f"Hello {datetime.datetime.now()}", flush=True)

print(os.getenv('mypass', None))
print(os.getenv('mongoConnectionString', None))

while True:
    process()
    time.sleep(20)



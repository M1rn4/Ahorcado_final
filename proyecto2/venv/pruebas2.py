import time
def timer():
   now = time.localtime(time.time())
   return now[5]

print(timer())



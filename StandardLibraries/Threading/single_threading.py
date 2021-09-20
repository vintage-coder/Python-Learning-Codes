import time
import threading

COUNT=50000000

def countdown(n):

    while n>=0:
        n-=1

start=time.time()

countdown(COUNT)

end=time.time()

print('time elapsed: ',end-start)




import time
import threading


COUNT=50000000


def countdown(n):
    while n>=0:
        n-=1


t1=threading.Thread(target=countdown,args=(COUNT//2,))

t2=threading.Thread(target=countdown,args=(COUNT//2,))

start =time.time()
t1.start()
t2.start()

t1.join()
t2.join()

end=time.time()


print('Time elapsed in multithreading: %f '%(end-start))

# In Python due to GIL(Global interpretor lock), multi threading can't be achieved...

# We can improve the process by multiprocessing





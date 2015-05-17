"""
Testing multiprocessing, redis
"""

# Imports
import redis
from multiprocessing import Queue, Pool, Lock


# initializing objects to be consumed.
Q = Queue()
container = [1, 2, 3, 4, 5, 1, 3, 4, 7, 1, 2, 6, 7, 94, 93, 234, 543, 1, 94, 94, 5]
for element in container:
    Q.put(element)

# initializing redis server
REDIS = redis.Redis("localhost")

# initializing the lock
LOCK = Lock()
# number of workers
NUM_WORKERS = 4

def f(x):
    elem = Q.get()
    LOCK.acquire()
    ret = REDIS.get(elem)
    LOCK.release()
    if ret != None:
        return ret
    else:
        LOCK.acquire()
        REDIS.set(elem, int(pow(x, 2)))
        LOCK.release()
        return int(pow(elem, 2))


p = Pool(NUM_WORKERS)
p.map(f, range(Q.qsize()))

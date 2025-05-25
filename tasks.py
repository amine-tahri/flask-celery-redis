# tasks.py
import time
import redis
from celery import Celery
from functools import wraps

# Connect Celery to Redis
celery = Celery(
    'tasks',
    broker='redis://localhost:6379/7',
    backend='redis://localhost:6379/7'
)

r = redis.from_url('redis://localhost:6379/7')

def with_redis_lock(auto_release_seconds:int):
    # one instance of a task should be scheduled at a time using a locking-system
    # try to acquire a lock using lock_key in redis
    # if the lock is acquired the task is exceuted
    # lock will be auto-released after auto_release_seconds
    # lock will be released when task ends with success or fail
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwrags):
            lock_key = f"lock:{func.__name__}"
            lock_acquired = r.set(lock_key, 1, nx=True, ex=auto_release_seconds)
            if not lock_acquired:
                # ignore task if a lock is already set
                return f"Task ignored: {func.__name__} already running"
            try:
                return func(*args, **kwrags)
            finally:
                r.delete(lock_key)
        return wrapper
    return decorator

@celery.task
@with_redis_lock(auto_release_seconds=900)
def add(x, y):
    time.sleep(10)
    return x + y

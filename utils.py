import time
import redis


cache = redis.StrictRedis(host='redis', decode_responses=True, db=0, port=6379)


def update_and_get_hit_count():
    """"""
    print('In utils/update_and_get_hit_count')
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as err:
            if retries == 0:
                raise err
            retries -= 1
            time.sleep(0.5)


def clear_hit_count():
    """"""

    print('in utils/clear_hit_count')
    retries = 5
    while True:
        try:
            return cache.set('hits', 0)
        except redis.exceptions.ConnectionError as err:
            if retries == 0:
                raise err
            retries -= 1
            time.sleep(0.5)

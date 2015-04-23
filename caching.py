import datetime

CACHE = {}

__all__ = ['write', 'read']

def write(key, value, expires):
    """
    Caches a value under a given key that will expire in *at least* a given amount of time

    If an entry already exists for a key, and will expire later than the given
    expire time, the first value is used, and the return value will be `False`.

    On writing a new value, if a current value exists but is expired, the
    current value will be removed, and the new value written.

    Args:
        key - name of the item to cache
        value - the actual value to cache
        expires = a python Datetime (tz-naive) object for when to clear the key
    Returns:
        Boolean - True on successful write, False if a longer-lived value is written
    """
    global CACHE
    value_dict = None
    try:
        value_dict = CACHE[key]
    except KeyError:
        pass

    if value_dict and value_dict.has_key('expires'):
        now = datetime.datetime.now()
        if now > value_dict['expires']:
            CACHE.pop(key)
        # The current expiry is later than the provided one.
        if expires < value_dict['expires']:
            return False

    value_dict = {'value': value, 'expires': expires}
    CACHE[key] = value_dict
    return True


def read(key):
    """
    Returns a value for a given key in the cache.

    If the key is present, and is not expired, the value will be returned

    If the value at the given key is expired, it will be removed from the
    cache and None will be returned.

    If no value exists for a given key, then None will be returned
    """
    global CACHE
    try:
        value_dict = CACHE[key]
    except KeyError:
        return None

    value, expires = value_dict['value'], value_dict['expires']

    now = datetime.datetime.now()
    if now > expires:
        # Value is old, so we shouldn't give it back.
        CACHE.pop(key)
        return None

    return value


def clear():
    """
    Empties the cache entirely
    """
    global CACHE
    CACHE = {}

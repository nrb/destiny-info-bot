import datetime

import caching as cache

today = datetime.datetime.today()
yesterday = today + datetime.timedelta(days=-1)
tomorrow = today +datetime.timedelta(days=1)

def teardown_function(function):
    cache.clear()


def test_write():
    cache.write('test', '92', tomorrow)
    value = cache.read('test')
    assert value == '92'


def test_reading_expires_old_value():
    cache.write('test', '1', yesterday)
    value = cache.read('test')
    assert value == None


def test_writing_expires_old_value():
    cache.write('test', '1', yesterday)
    cache.write('test', '2', tomorrow)
    value = cache.read('test')
    assert value == '2'


def test_reading_nonexistent_key():
    val = cache.read('test')
    assert val is None


def test_writing_with_newer_expire():
    cache.write('test', '1', tomorrow)
    result = cache.write('test', '2', today)
    assert result == False

    val = cache.read('test')
    assert val == '1'

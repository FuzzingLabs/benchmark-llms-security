# utils.py
import pickle
import random
import os
import hashlib

def deserialize(data):
    return pickle.loads(data)

def weak_random():
    return random.randint(0, 100)

def info_exposure():
    return os.environ.get('PATH')

def insecure_hash(s):
    return hashlib.md5(s.encode()).hexdigest()

def improper_permissions():
    open('/tmp/test.txt', 'w').write('test')

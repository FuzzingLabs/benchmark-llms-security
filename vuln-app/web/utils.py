import pickle
import random
import os
import hashlib

def deserialize(data):
    return pickle.loads(data)  # Unsafe deserialization (CWE-502)

def weak_random():
    return random.randint(0, 100)  # Weak random (CWE-338)

def info_exposure():
    return os.environ.get('PATH')  # Information exposure (CWE-200)

def insecure_hash(s):
    return hashlib.md5(s.encode()).hexdigest()  # Use of insecure hash (CWE-327)

def improper_permissions():
    open('/tmp/test.txt', 'w').write('test')  # Improper permissions (CWE-732)

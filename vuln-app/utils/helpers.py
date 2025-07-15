# helpers.py
import random

def log_sensitive(data):
    print('Sensitive:', data)

def insecure_random():
    return random.randint(0, 1000000)

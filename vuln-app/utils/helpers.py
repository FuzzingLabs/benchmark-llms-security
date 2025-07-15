import random

def log_sensitive(data):
    print('Sensitive:', data)  # Logging sensitive data (CWE-532)

def insecure_random():
    return random.randint(0, 1000000)  # Insecure random (CWE-338)

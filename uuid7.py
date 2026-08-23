import time, os
def gen(): return f'{int(time.time()*1000):012x}-{os.urandom(6).hex()}'
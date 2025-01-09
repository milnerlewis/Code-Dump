import random
import time

num = 3

while True:
    print([[random.randint(0,9)] * 1 for a in range(num)])
    time.sleep(0.05)
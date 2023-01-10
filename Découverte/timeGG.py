# https://www.programiz.com/python-programming/time

import time

def il_est_lheure():
    secondes = time.time()
    temps = time.ctime(secondes)
    print(temps)
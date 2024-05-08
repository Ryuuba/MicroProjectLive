"""This module holds functions to test the functionality of this project
"""
from digital_clock import DigitalClock
from utime import sleep

def clock_test() -> None:
    clock = DigitalClock()
    while True:
        h, m, s = clock.get_time()
        time = f'{h:02} : {m:02} : {s:02}'
        print(time)
        sleep(1)
        clock.increment()

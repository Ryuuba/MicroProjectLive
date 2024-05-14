"""This module holds functions to test the functionality of this project
"""
from digital_clock import DigitalClock
from utime import sleep
from random import randint
from fsm import FSM

def clock_test() -> None:
    clock = DigitalClock(23, 59, 40)
    while True:
        h, m, s = clock.get_time()
        time = f'{h:02} : {m:02} : {s:02}'
        print(time)
        sleep(1)
        clock.increment()

def fsm_test() -> None:
    fsm = FSM()
    event = {
        'unconditional':    0,
        'default':          1,
        'press button':     2,
        'button':           3,
        'not button':       4,
        'not timeout':      5
        #timeout event is handled by the interrupt uC interrupt mechanism
    }
    fsm.set_transition_rule(0, event['unconditional'], 1)
    fsm.set_transition_rule(1, event['default'], 1)
    fsm.set_transition_rule(1, event['press button'], 2)
    fsm.set_transition_rule(2, event['button'], 4)
    fsm.set_transition_rule(2, event['not button'], 1)
    fsm.set_transition_rule(4, event['not timeout'], 5)
    fsm.set_transition_rule(5, event['not timeout'], 1)
    while True:
        state = fsm.get_current_state()
        if state == 0:
            print(f'current state {state}')
            sleep(1)
            fsm.compute_next_state(event['unconditional'])
        elif state == 1:
            print(f'current state {state}')
            sleep(1)
            rnd_ev = randint(event['default'], event['press button'])
            fsm.compute_next_state(rnd_ev)
        elif state == 2:
            print(f'current state {state}')
            sleep(1)
            rnd_ev = randint(event['button'], event['not button'])
            fsm.compute_next_state(rnd_ev)
        # state three is handled by interrupting the uC
        elif state == 4:
            print(f'current state {state}')
            sleep(1)
            fsm.compute_next_state(event['not timeout'])
        elif state == 5:
            print(f'current state {state}')
            sleep(1)
            fsm.compute_next_state(event['not timeout'])
        else:
            print('Are you OK, Any?')
            break        





































from time_handling import *


def _init_datetime_object() -> datetime:
    datetime_object = datetime
    return datetime_object


def get_time_shift_direction() -> str:
    direction = str(input("Would you like to (D)elay or (A)dvance the subtitle file? Answer here : "))
    direction.lower()
    if direction == "d":
        direction = "delay"
        print("Prompt : This file will be (d)elayed")
        return direction
    elif direction == "a":
        direction = "advance"
        print("Prompt : This file will be (a)dvanced")
        return direction
    else:
        print("Prompt : Input not understood, please enter \"a\" or \"d\"")
        get_time_shift_direction()


def get_time_shift_seconds_input() -> datetime:
    time_shift = _init_datetime_object()
    try:
        time_shift.second = datetime(input("Enter desired time shift seconds using integer values : "))
    except RuntimeError:
        raise RuntimeError
    if time_shift.second < 0 or time_shift.second > 60:
        raise Exception
    return time_shift.second



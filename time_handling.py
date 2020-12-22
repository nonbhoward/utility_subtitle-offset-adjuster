from datetime import datetime
from datetime import timedelta


def get_datetime_timeshift(hour: int, minute: int, second: int):
    if second_has_millis(second):
        second, millis = str(second).split('.', 2)[0], str(second).split('.', 2)[1]
        datetime_timeshift = datetime(year=1, month=1, day=1,
                                      hour=hour, minute=minute,
                                      second=int(second), microsecond=int(millis)*1000)
        return datetime_timeshift
    datetime_timeshift = datetime(year=1, month=1, day=1,
                                  hour=hour, minute=minute, second=int(second))
    return datetime_timeshift


def second_has_millis(second):
    if '.' in str(second):
        return True
    return False


def shift_datetime_by_timeshift(unshifted_datetime: datetime, time_shift: datetime) -> datetime:
    shifted_timestamp = unshifted_datetime + timedelta(hours=time_shift.hour)
    shifted_timestamp = unshifted_datetime + timedelta(minutes=time_shift.minute)
    shifted_timestamp = unshifted_datetime + timedelta(seconds=time_shift.second)
    return shifted_timestamp

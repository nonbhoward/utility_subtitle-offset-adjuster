from datetime import datetime


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


def shift_timestamp_by_time_shift(unshifted_hours: list,
                                  unshifted_minutes: list,
                                  unshifted_seconds: list,
                                  unshifted_millis: list,
                                  time_shift: datetime) -> datetime:
    start_hour = datetime.hour(unshifted_hours[0])
    stop_hour = datetime.hour(unshifted_hours[1])
    start_minute = datetime.minute(unshifted_minutes[0])
    stop_minute = datetime.minute(unshifted_minutes[1])
    start_second = datetime.second(unshifted_seconds[0])
    stop_second = datetime.second(unshifted_seconds[1])
    start_millis = datetime.microsecond(unshifted_millis[0]*1000)
    stop_millis = datetime.microsecond(unshifted_millis[1]*1000)

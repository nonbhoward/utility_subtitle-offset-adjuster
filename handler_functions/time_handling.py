from datetime import datetime
from datetime import timedelta
from minimalog.minimal_log import MinimalLog
mlog = MinimalLog(__name__)


def get_datetime_timeshift(hour: int, minute: int, second: int):
    build_event = 'create datetime object from timeshift input'
    mlog.log_event(build_event, event_completed=False)
    if not 0 <= second < 60:
        print('exception, seconds offset must be between 0 and 60')
        raise ArithmeticError
    if _seconds_has_millis(second):
        second, millis = str(second).split('.', 2)[0], str(second).split('.', 2)[1]
        datetime_timeshift = datetime(year=1, month=1, day=1,
                                      hour=hour, minute=minute,
                                      second=int(second), microsecond=int(millis)*1000)
        mlog.log_event(build_event, event_completed=True)
        return datetime_timeshift
    datetime_timeshift = datetime(year=1, month=1, day=1,
                                  hour=hour, minute=minute, second=int(second))
    mlog.log_event(build_event, event_completed=True)
    return datetime_timeshift


def shift_datetimes_by_timeshift(unshifted_datetimes: list, time_shift: datetime) -> list:
    # TODO bug : seconds can only be positive
    # TODO bug : hours and seconds cannot be entered
    shifted_timestamp_start = unshifted_datetimes[0] + timedelta(hours=time_shift.hour)
    shifted_timestamp_start = unshifted_datetimes[0] + timedelta(minutes=time_shift.minute)
    shifted_timestamp_start = unshifted_datetimes[0] + timedelta(seconds=time_shift.second)
    shifted_timestamp_stop = unshifted_datetimes[1] + timedelta(hours=time_shift.hour)
    shifted_timestamp_stop = unshifted_datetimes[1] + timedelta(minutes=time_shift.minute)
    shifted_timestamp_stop = unshifted_datetimes[1] + timedelta(seconds=time_shift.second)
    return [shifted_timestamp_start, shifted_timestamp_stop]


def _seconds_has_millis(second):
    mlog.log_event('checking if timeshift offset contains milliseconds')
    if '.' in str(second):
        return True
    return False


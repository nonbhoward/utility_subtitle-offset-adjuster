from datetime import datetime

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




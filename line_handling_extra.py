from line_handling import _fetch_hours_from_timestamp
from line_handling import _fetch_minutes_from_timestamp
from line_handling import _fetch_seconds_from_timestamp
from line_handling import _fetch_millis_from_timestamp
from line_handling import _is_timestamp_line


def _build_zipped_timestamps(file_contents: list) -> zip:  # only a test
    hour_list, minute_list, second_list, milli_list = [], [], [], []
    for line_from_file in file_contents:
        if _is_timestamp_line(line_from_file):
            hour_list.append(_fetch_hours_from_timestamp(line_from_file))
            minute_list.append(_fetch_minutes_from_timestamp(line_from_file))
            second_list.append(_fetch_seconds_from_timestamp(line_from_file))
            milli_list.append(_fetch_millis_from_timestamp(line_from_file))
    return zip(hour_list, minute_list, second_list, milli_list)


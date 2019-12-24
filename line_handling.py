# #####UNPARSED TEXT EXAMPLE######
# 1
# 00:00:00,000 --> 00:00:00,000
# I am a line of subtitle text
#
# 2
# 00:00:00,000 --> 00:00:00,000
# I am a second line of subtitles
#
# 3
# #####UNPARSED TEXT EXAMPLE######
import datetime, re
global delimiter
delimiter = "-->"


def build_timestamps_zip(file_contents: list) -> zip:
    hour_list, minute_list, second_list, milli_list = [], [], [], []
    for line_from_file in file_contents:
        if _identify_timestamp_line(line_from_file):
            hour_list.append(_filter_hours(line_from_file))
            minute_list.append(_filter_minutes(line_from_file))
            second_list.append(_filter_seconds(line_from_file))
            milli_list.append(_filter_millis(line_from_file))
    return [hour_list, minute_list, second_list, milli_list]


def _filter_hours(timestamp_line: str) -> list:
    regex_hour = "^\d\d"
    start_hour = str(re.findall(regex_hour, timestamp_line.split(delimiter)[0].strip()))
    stop_hour = str(re.findall(regex_hour, timestamp_line.split(delimiter)[1].strip()))
    return [start_hour, stop_hour]


def _filter_millis(timestamp_line: str) -> list:
    regex_millisec = "\d\d\d"
    start_millisec = str(re.findall(regex_millisec, timestamp_line.split(delimiter)[0].strip()))
    stop_millisec = str(re.findall(regex_millisec, timestamp_line.split(delimiter)[1].strip()))
    return [start_millisec, stop_millisec]


def _filter_minutes(timestamp_line: str) -> list:
    regex_minute = ":\d\d:"
    start_minute = str(re.findall(regex_minute, timestamp_line.split(delimiter)[0].strip()))
    start_minute = start_minute.replace(regex_minute[0], '')
    stop_minute = str(re.findall(regex_minute, timestamp_line.split(delimiter)[1].strip()))
    stop_minute = stop_minute.replace(regex_minute[-1], '')
    return [start_minute, stop_minute]


def _filter_seconds(timestamp_line: str) -> list:
    regex_sec = ":\d\d,"
    start_second = str(re.findall(regex_sec, timestamp_line.split(delimiter)[0].strip()))
    start_second = start_second.replace(regex_sec[0], '').replace(regex_sec[-1], '')
    stop_second = str(re.findall(regex_sec, timestamp_line.split(delimiter)[1].strip()))
    stop_second = stop_second.replace(regex_sec[0], '').replace(regex_sec[-1], '')
    return [start_second, stop_second]


def _identify_timestamp_line(line_from_file: str) -> str:
    if line_from_file.count(":") == 4 and line_from_file.count(",") == 2:
        return True  # this is a timestamp line
    else:
        return False  # this is NOT a timestamp line



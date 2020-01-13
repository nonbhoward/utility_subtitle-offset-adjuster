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
import datetime
import re

global delimiter
delimiter = "-->"


def build_shifted_subtitle(file_contents: list, time_shift: datetime) -> list:
    shifted_sub = []
    for line_from_file in file_contents:
        stripped_line = line_from_file.strip()
        line_is_sequence = _is_sequence_line(stripped_line)
        line_is_timestamp = _is_timestamp_line(stripped_line)
        if line_is_sequence:
            shifted_sub.append(stripped_line)
        elif line_is_timestamp:
            # todo datetime shift function here
            shifted_sub.append(stripped_line)
        elif _is_subtitle_line(stripped_line):
            shifted_sub.append(stripped_line)
        else:
            shifted_sub.append("LINE TYPE UNKNOWN")
    return shifted_sub


def _fetch_hours_from_timestamp(timestamp_line: str) -> list:
    regex_hour = "^\d\d"
    start_hour = str(re.findall(regex_hour, timestamp_line.split(delimiter)[0].strip()))
    stop_hour = str(re.findall(regex_hour, timestamp_line.split(delimiter)[1].strip()))
    return [start_hour, stop_hour]


def _fetch_millis_from_timestamp(timestamp_line: str) -> list:
    regex_millisec = "\d\d\d"
    start_millisec = str(re.findall(regex_millisec, timestamp_line.split(delimiter)[0].strip()))
    stop_millisec = str(re.findall(regex_millisec, timestamp_line.split(delimiter)[1].strip()))
    return [start_millisec, stop_millisec]


def _fetch_minutes_from_timestamp(timestamp_line: str) -> list:
    regex_minute = ":\d\d:"
    start_minute = str(re.findall(regex_minute, timestamp_line.split(delimiter)[0].strip()))
    start_minute = start_minute.replace(regex_minute[0], '')
    stop_minute = str(re.findall(regex_minute, timestamp_line.split(delimiter)[1].strip()))
    stop_minute = stop_minute.replace(regex_minute[-1], '')
    return [start_minute, stop_minute]


def _fetch_seconds_from_timestamp(timestamp_line: str) -> list:
    regex_sec = ":\d\d,"
    start_second = str(re.findall(regex_sec, timestamp_line.split(delimiter)[0].strip()))
    start_second = start_second.replace(regex_sec[0], '').replace(regex_sec[-1], '')
    stop_second = str(re.findall(regex_sec, timestamp_line.split(delimiter)[1].strip()))
    stop_second = stop_second.replace(regex_sec[0], '').replace(regex_sec[-1], '')
    return [start_second, stop_second]


# an iterator line numbers each subtitle appearance
def _is_sequence_line(line_from_file: str) -> bool:
    regex_sequence_number = "^[\d]+$"  # match any number (+) of \d AND do NOT (^) match \d\d:
    if re.match(regex_sequence_number, line_from_file):
        return True
    else:
        return False


# a subtitle line contains a subtitle to be displayed (or an empty line?)  # fixme handle empty lines better
def _is_subtitle_line(line_from_file: str) -> bool:
    # regex_subtitle = ""  # todo maybe later, identifying timestamps is probably enough for program function
    if not _is_sequence_line(line_from_file) and not _is_timestamp_line(line_from_file):
        return True
    else:
        return False


# a timestamp line contains two timestamps: a start-time and a stop-time between which a subtitle will be displayed
def _is_timestamp_line(line_from_file: str) -> bool:
    regex_timestamp = "[\d]+:[\d]+:[\d]+,[\d]+\s[-]+[>]\s[\d]+:[\d]+:[\d]+,[\d]+"
    if re.match(regex_timestamp, line_from_file):
        return True
    else:
        return False

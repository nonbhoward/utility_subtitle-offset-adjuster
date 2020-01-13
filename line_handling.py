﻿# #####UNPARSED TEXT EXAMPLE######
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


def build_shifted_subtitle(file_contents: list, time_shift: datetime) -> list:
    shifted_sub = []
    iteration = 1
    for line_from_file in file_contents:
        stripped_line = line_from_file.strip()
        line_is_sequence_number = _is_sequence_number(stripped_line, iteration)
        line_is_timestamp = _is_timestamp_line(stripped_line)
        line_is_subtitle = _is_subtitle_line(not line_is_sequence_number, not line_is_timestamp)
        shifted_sub.append("DEBUG : Iterator : " + str(line_is_sequence_number) +
                           ", Timestamp : " + str(line_is_timestamp) +
                           ", Subtitle : " + str(line_is_subtitle))
        if line_is_sequence_number:
            shifted_sub.append(stripped_line + str(_is_sequence_number()))  # fixme wrong function call syntax
            iteration += 1
        elif line_is_timestamp:
            # todo datetime shift function here
            shifted_sub.append(stripped_line)
        elif line_is_subtitle:
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
def _is_sequence_number(line_from_file: str, sequence: int) -> bool:  # fixme this is never true
    regex_sequence_number = ""
    return False


# a subtitle line contains a subtitle to be displayed (or an empty line?)  # fixme handle empty lines better
def _is_subtitle_line(line_not_iterator: bool, line_not_timestamp: bool) -> bool:
    regex_subtitle_line = ""
    return False


# a timestamp line contains two timestamps: a start-time and a stop-time between which a subtitle will be displayed
def _is_timestamp_line(line_from_file: str) -> bool:
    regex_timestamp_line = ""
    return False


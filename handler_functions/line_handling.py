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
from handler_functions.time_handling import *
from minimalog.minimal_log import MinimalLog
import datetime
import re
mlog = MinimalLog(__name__)

delimiter = "-->"


def build_shifted_subtitle(file_contents: list, time_shift: datetime) -> list:
    sub_build_event = 'building shifted subtitle'
    mlog.log_event(sub_build_event, event_completed=False)
    shifted_sub = []
    current_sequence = 1  # this iterates once each time a subtitle is displayed on the screen
    for line_from_file in file_contents:
        stripped_line = line_from_file.strip()
        # mlog.log_event('processing line : ' + stripped_line)
        if _is_empty_line(stripped_line):
            shifted_sub.append("")
        elif _is_sequence_line(stripped_line, current_sequence):
            shifted_sub.append(stripped_line)  # only to rebuild new file
            current_sequence += 1
        elif _is_timestamp_line(stripped_line):
            unshifted_datetimes = _get_datetimes(line_from_file)
            shifted_datetimes = shift_datetimes_by_timeshift(unshifted_datetimes, time_shift)
            shifted_timestamp_line = rebuild_shifted_datetime_to_timestamp(shifted_datetimes)
            shifted_sub.append(shifted_timestamp_line)
        elif _is_subtitle_line(stripped_line):
            shifted_sub.append(stripped_line)  # only to rebuild new file
        else:
            if len(shifted_sub) < 1:
                continue
            shifted_sub.append("LINE TYPE UNKNOWN")
    mlog.log_event(sub_build_event, event_completed=True)
    return shifted_sub


def rebuild_shifted_datetime_to_timestamp(shifted_datetimes: datetime) -> str:
    space = " "
    built_timestamp_start = str(f"{int(shifted_datetimes[0].hour):02d}") + ":" + \
                            str(f"{int(shifted_datetimes[0].minute):02d}") + ":" + \
                            str(f"{int(shifted_datetimes[0].second):02d}") + "," + \
                            str(f"{int(shifted_datetimes[0].microsecond):03d}")
    built_timestamp_stop = str(f"{int(shifted_datetimes[1].hour):02d}") + ":" + \
                           str(f"{int(shifted_datetimes[1].minute):02d}") + ":" + \
                           str(f"{int(shifted_datetimes[1].second):02d}") + "," + \
                           str(f"{int(shifted_datetimes[1].microsecond):03d}")
    built_timestamp = built_timestamp_start.rstrip('000') + \
                      space + delimiter + space + \
                      built_timestamp_stop.rstrip('000')
    return built_timestamp


def _compile_regex():
    compile_event = 'compiling regex'
    mlog.log_event(compile_event)
    regex_pattern_for_empty_lines, \
        regex_pattern_for_sequence_lines, \
        regex_pattern_for_subtitle_lines = "^\s*$", \
                                           "^\d{1,5}$", \
                                           "[\d]+:[\d]+:[\d]+,[\d]+\s[-]+[>]\s[\d]+:[\d]+:[\d]+,[\d]+"
    regex_empty_line, \
        regex_sequence_line, \
        regex_subtitle_line = re.compile(regex_pattern_for_empty_lines), \
                              re.compile(regex_pattern_for_sequence_lines), \
                              re.compile(regex_pattern_for_subtitle_lines)
    return regex_empty_line, regex_sequence_line, regex_subtitle_line


def _fetch_hour_start_from_timestamp(hours: list) -> int:
    stripped_hour = hours[0].replace('\'', '')
    stripped_hour = stripped_hour.replace('[', '')
    stripped_hour = int(stripped_hour.replace(']', ''))
    return stripped_hour


def _fetch_hour_stop_from_timestamp(hours: list) -> int:
    stripped_hour = hours[1].replace('\'', '')
    stripped_hour = stripped_hour.replace('[', '')
    stripped_hour = int(stripped_hour.replace(']', ''))
    return stripped_hour


def _fetch_hours_from_timestamp(timestamp_line: str) -> list:
    regex_hour = "^\d\d"
    start_hour = str(re.findall(regex_hour, timestamp_line.split(delimiter)[0].strip()))
    stop_hour = str(re.findall(regex_hour, timestamp_line.split(delimiter)[1].strip()))
    return [start_hour, stop_hour]


def _fetch_millis_start_from_timestamp(timestamp_line: list) -> int:
    stripped_milli = timestamp_line[0].replace('\'', '')
    stripped_milli = stripped_milli.replace('[', '')
    stripped_milli = int(stripped_milli.replace(']', ''))
    return stripped_milli * 1000


def _fetch_millis_stop_from_timestamp(timestamp_line: list) -> int:
    stripped_milli = timestamp_line[1].replace('\'', '')
    stripped_milli = stripped_milli.replace('[', '')
    stripped_milli = int(stripped_milli.replace(']', ''))
    return stripped_milli * 1000


def _fetch_millis_from_timestamp(timestamp_line: str) -> list:
    regex_millisec = "\d\d\d"
    start_millisec = str(re.findall(regex_millisec, timestamp_line.split(delimiter)[0].strip()))
    stop_millisec = str(re.findall(regex_millisec, timestamp_line.split(delimiter)[1].strip()))
    return [start_millisec, stop_millisec]


def _fetch_minutes_start_from_timestamp(minutes: list) -> int:
    stripped_minute = minutes[0].replace('\'', '')
    stripped_minute = stripped_minute.replace('[', '')
    stripped_minute = int(stripped_minute.replace(']', ''))
    return stripped_minute


def _fetch_minutes_stop_from_timestamp(minutes: list) -> int:
    stripped_minute = minutes[1].replace('\'', '')
    stripped_minute = stripped_minute.replace('[', '')
    stripped_minute = int(stripped_minute.replace(']', ''))
    return stripped_minute


def _fetch_minutes_from_timestamp(timestamp_line: str) -> list:
    regex_minute = ":\d\d:"
    start_minute = str(re.findall(regex_minute, timestamp_line.split(delimiter)[0].strip()))
    start_minute = start_minute.replace(regex_minute[0], '')
    stop_minute = str(re.findall(regex_minute, timestamp_line.split(delimiter)[1].strip()))
    stop_minute = stop_minute.replace(regex_minute[-1], '')
    return [start_minute, stop_minute]


def _fetch_seconds_start_from_timestamp(seconds: list) -> int:
    stripped_seconds = seconds[0].split(',')[0]
    stripped_seconds = stripped_seconds.replace('\'', '')
    stripped_seconds = stripped_seconds.replace('[', '')
    stripped_seconds = int(stripped_seconds.replace(']', ''))
    return stripped_seconds


def _fetch_seconds_stop_from_timestamp(seconds: list) -> int:
    stripped_seconds = seconds[1].split(',')[0]
    stripped_seconds = stripped_seconds.replace('\'', '')
    stripped_seconds = stripped_seconds.replace('[', '')
    stripped_seconds = int(stripped_seconds.replace(']', ''))
    return stripped_seconds


def _fetch_seconds_from_timestamp(timestamp_line: str) -> list:
    regex_sec = ":\d{2},\d{3}"
    start_second = str(re.findall(regex_sec, timestamp_line.split(delimiter)[0].strip()))
    start_second = start_second.replace(regex_sec[0], '').replace(regex_sec[-1], '')
    stop_second = str(re.findall(regex_sec, timestamp_line.split(delimiter)[1].strip()))
    stop_second = stop_second.replace(regex_sec[0], '').replace(regex_sec[-1], '')
    return [start_second, stop_second]


def _get_datetimes(line_from_file: str) -> list:
    dt_start = datetime.datetime(year=1, month=1, day=1,
                                 hour=_fetch_hour_start_from_timestamp(_fetch_hours_from_timestamp(line_from_file)),
                                 minute=_fetch_minutes_start_from_timestamp(_fetch_minutes_from_timestamp(line_from_file)),
                                 second=_fetch_seconds_start_from_timestamp(_fetch_seconds_from_timestamp(line_from_file)),
                                 microsecond=_fetch_millis_start_from_timestamp(_fetch_millis_from_timestamp(line_from_file)))
    dt_stop = datetime.datetime(year=1, month=1, day=1,
                                hour=_fetch_hour_stop_from_timestamp(_fetch_hours_from_timestamp(line_from_file)),
                                minute=_fetch_minutes_stop_from_timestamp(_fetch_minutes_from_timestamp(line_from_file)),
                                second=_fetch_seconds_stop_from_timestamp(_fetch_seconds_from_timestamp(line_from_file)),
                                microsecond=_fetch_millis_stop_from_timestamp(_fetch_millis_from_timestamp(line_from_file)))
    return [dt_start, dt_stop]


def _is_empty_line(line_from_file: str) -> bool:
    if empty_line_finder.search(line_from_file):
        return True
    return False


def _is_sequence_line(line_from_file: str, current_sequence: int) -> bool:
    # TODO for some reason if the line being checked is the first line in the file, this test fails
    if sequence_line_finder.search(line_from_file):
        if int(line_from_file) == current_sequence:
            return True
    return False


# a subtitle line contains a subtitle to be displayed (or an empty line?)  # fixme handle empty lines better
def _is_subtitle_line(line_from_file: str) -> bool:
    found = subtitle_line.match(line_from_file)
    if not _is_sequence_line(line_from_file, current_sequence=999) and not _is_timestamp_line(line_from_file):
        return True
    return False


# a timestamp line contains two timestamps: a start-time and a stop-time between which a subtitle will be displayed
def _is_timestamp_line(line_from_file: str) -> bool:
    if subtitle_line.search(line_from_file):
        return True
    return False


empty_line_finder, sequence_line_finder, subtitle_line = _compile_regex()

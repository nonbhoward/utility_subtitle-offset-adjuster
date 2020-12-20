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

delimiter = "-->"


def build_shifted_subtitle(file_contents: list, time_shift: datetime) -> list:
    shifted_sub = []
    current_sequence = 1  # this iterates once each time a subtitle is displayed on the screen
    for line_from_file in file_contents:
        stripped_line = line_from_file.strip()
        if _is_empty_line(stripped_line):
            shifted_sub.append("")
        elif _is_sequence_line(stripped_line, current_sequence):
            shifted_sub.append(stripped_line)  # only to rebuild new file
            current_sequence += 1
        elif _is_timestamp_line(stripped_line):
            unshifted_hours = _fetch_hours_from_timestamp(stripped_line)
            unshifted_minutes = _fetch_minutes_from_timestamp(stripped_line)
            unshifted_seconds = _fetch_seconds_from_timestamp(stripped_line)
            unshifted_millis = _fetch_millis_from_timestamp(stripped_line)
            # todo datetime shift function here
            shift_timestamp_by_time_shift(unshifted_hours,
                                          unshifted_minutes,
                                          unshifted_seconds,
                                          unshifted_millis,
                                          time_shift)
            shifted_sub.append(stripped_line)
        # elif _is_subtitle_line(stripped_line):
        #     shifted_sub.append(stripped_line)  # only to rebuild new file
        else:
            if len(shifted_sub) < 1:
                continue
            shifted_sub.append("LINE TYPE UNKNOWN")
    return shifted_sub


def compile_regex():
    regex_sequence_for_empty_lines, \
        regex_pattern_for_sequence_lines, \
        regex_sequence_for_subtitle_lines = "^\s*$", "^\d{1,5}$", "TODO"
    regex_empty_line, \
        regex_sequence_line, \
        regex_subtitle_line = re.compile(regex_sequence_for_empty_lines), \
                              re.compile(regex_pattern_for_sequence_lines), \
                              re.compile(regex_sequence_for_subtitle_lines)
    return regex_empty_line, regex_sequence_line, regex_subtitle_line


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


def _is_empty_line(line_from_file: str) -> bool:
    if empty_line_finder.search(line_from_file):
        return True
    return False


def _is_sequence_line(line_from_file: str, current_sequence: int) -> bool:
    # TODO for some reason if the line being checked is the first line in the file, this test fails
    found = sequence_line_finder.search(line_from_file)
    if found:
        if int(line_from_file) == current_sequence:
            return True
    return False


# a subtitle line contains a subtitle to be displayed (or an empty line?)  # fixme handle empty lines better
def _is_subtitle_line(line_from_file: str) -> bool:
    found = subtitle_line.match(line_from_file)
    if not _is_sequence_line(line_from_file) and not _is_timestamp_line(line_from_file):
        return True
    return False


# a timestamp line contains two timestamps: a start-time and a stop-time between which a subtitle will be displayed
def _is_timestamp_line(line_from_file: str) -> bool:
    regex_timestamp = "[\d]+:[\d]+:[\d]+,[\d]+\s[-]+[>]\s[\d]+:[\d]+:[\d]+,[\d]+"
    if re.match(regex_timestamp, line_from_file):
        return True
    return False


empty_line_finder, sequence_line_finder, subtitle_line = compile_regex()

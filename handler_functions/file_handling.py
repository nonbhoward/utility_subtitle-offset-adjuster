from minimalog.minimal_log import MinimalLog
from subtitle_class import *
import os
import pathlib
import sys
mlog = MinimalLog(__name__)


def filter_subtitle_files(working_dir_file_list: list) -> str:
    mlog.log_event('filtering subtitle file')
    try:
        sub_file = Subtitle()
        for file in working_dir_file_list:
            if str(file).lower().endswith(sub_file.get_file_extension()):
                sub_file.filename = file
                return str(file)
        mlog.log_event('no subtitle file found, exiting program')
        sys.exit()
    except RuntimeError:
        mlog.log_event('error while filtering subtitle file')
        raise RuntimeError


def find_subtitle_file(file_extension: str) -> list:  # todo cwd limitation is restrictive
    mlog.log_event('finding subtitle file')
    try:
        working_dir = os.getcwd()  # get current working directory aka 'cwd'
        working_dir_file_list = os.listdir(working_dir)  # get list() of files in cwd
        return filter_subtitle_files(working_dir_file_list)
    except OSError:
        mlog.log_event('error while finding subtitle file')
        raise OSError


def open_subtitle_file(filename: list) -> list:
    mlog.log_event('opening subtitle file')
    try:
        sub_file = pathlib.Path(filename)
        print("Debug : Started reading from filename : " + str(filename))
        # debug # file_contents = read_file_contents(filename)
        file_contents_list = \
            read_file_contents_as_list(filename)
        return file_contents_list
    except RuntimeError:
        mlog.log_event('error opening subtitle file')
        raise RuntimeError


def read_file_contents_as_list(filename: str) -> list:
    file_event = 'reading file contents'
    mlog.log_event(file_event, event_completed=False)
    try:
        with open(filename, "r") as loaded_file:
            mlog.log_event(file_event, event_completed=True)
            return loaded_file.readlines()
    except FileNotFoundError:
        mlog.log_event('error reading file contents')
        raise FileNotFoundError


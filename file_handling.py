from subtitle import *
import os
import pathlib
import sys


def filter_subtitle_files(working_dir_file_list: list) -> str:
    try:
        sub_file = Subtitle()
        for file in working_dir_file_list:
            if str(file).lower().endswith(sub_file.get_file_extension()):
                sub_file.filename = file
                return str(file)
        print('no subtitle file found, exiting program')
        sys.exit()
    except RuntimeError:
        raise RuntimeError


def find_subtitle_file(file_extension: str) -> list:  # todo cwd limitation is restrictive
    try:
        working_dir = os.getcwd()  # get current working directory aka 'cwd'
        working_dir_file_list = os.listdir(working_dir)  # get list() of files in cwd
        return filter_subtitle_files(working_dir_file_list)
    except OSError:
        raise OSError


def open_subtitle_file(filename: list) -> list:
    try:
        sub_file = pathlib.Path(filename)
        print("Debug : Started reading from filename : " + str(filename))
        # debug # file_contents = read_file_contents(filename)
        file_contents_list = \
            read_file_contents_as_list(filename)
        return file_contents_list
    except RuntimeError:
        raise RuntimeError


def read_file_contents_as_list(filename: str) -> list:
    try:
        with open(filename, "r") as loaded_file:
            return loaded_file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError


import glob
import re
import shutil
import pathlib
import string


class Subtitle:
    def __init__(self, file_extension: str):
        self.file_extension = ".srt"

    def get_file_extension(self):
        return self.file_extension

    def set_file_extension(self, new_file_extension):
        self.file_extension = new_file_extension


def filter_subtitle_files(working_dir_file_list, file_extension):
    sub_file = Subtitle(file_extension)
    for file in working_dir_file_list:
        if str(file.name).endswith(sub_file.get_file_extension()):
            return file.name


def find_subtitle_file_with_extension(file_extension):
    # todo cwd limitation is restrictive? make a decision on this
    # deprecated # working_dir_file_list = os.scandir(os.getcwd())
    # returns files in cwd according to glob pattern
    working_dir_file_list = pathlib.Path.glob(pathlib.Path.cwd(), "*")
    return filter_subtitle_files(working_dir_file_list, file_extension)


def open_subtitle_file(filename: str):
    # todo check the file exists to avoid future errors
    print(read_file_contents(filename))
    # debug # print(read_file_contents(loaded_file))
    # debug # print(read_file_contents_by_line_range(loaded_file, line_start=10, line_end=13))
    print("Debug : Reading from filename " + str(filename))
    return None


def read_file_contents(filename: str):
    with open(filename, "r") as loaded_file:  # todo confirm that with-indent closes the file
        return repr(loaded_file.read())


def read_file_contents_by_line(loaded_file, line_number: int):
    for line in loaded_file.readline():
        print(line)
    # return loaded_file_line


def read_file_contents_by_line_range(loaded_file, line_start: int, line_end: int):
    loaded_file_line_range = loaded_file
    for _ in range(line_start, line_end):
        print(_)
        print(read_file_contents_by_line(loaded_file, _))
    return loaded_file_line_range


def set_subtitle_extension(file_extension):
    return file_extension  # fixme this makes no sense in current structure


def set_subtitle_dir(dir_path: str):
    os.chdir(dir_path)

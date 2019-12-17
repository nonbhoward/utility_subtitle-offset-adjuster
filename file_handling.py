import re
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


def find_subtitle_file_with_extension(file_extension):  # todo cwd limitation is restrictive
    # deprecated # working_dir_file_list = os.scandir(os.getcwd())
    # returns files in cwd according to glob(path, pattern)
    working_dir_file_list = pathlib.Path.glob(pathlib.Path.cwd(), "*")
    return filter_subtitle_files(working_dir_file_list, file_extension)


def open_subtitle_file(filename: str):  # todo check file exists
    # debug # print(read_file_contents(filename))
    for _ in range(15, 20):
        print(read_file_contents_by_line(filename, _))
    # debug # print(read_file_contents_by_line_range(loaded_file, line_start=10, line_end=13))
    print("Debug : Reading from filename " + str(filename))
    return None


def read_file_contents(filename: str):
    with open(filename, "r") as loaded_file:
        return repr(loaded_file.read())


def read_file_contents_by_line(filename, line_number: int):
    with open(filename, "r") as loaded_file:
        for line in loaded_file:
            if line.index == line_number:
                print(repr(loaded_file.readline()))


def read_file_contents_by_line_range(loaded_file, line_start: int, line_end: int):
    loaded_file_line_range = loaded_file
    for _ in range(line_start, line_end):
        print(_)
        print(read_file_contents_by_line(loaded_file, _))
    return loaded_file_line_range


def set_subtitle_extension(file_extension):  # fixme makes no sense, delete or make useful
    return file_extension


def set_subtitle_dir(dir_path: str):  # todo untested
    # is this better? # os.chdir(dir_path)
    cwd_path = pathlib.Path(dir_path)
    pathlib.Path(cwd_path)

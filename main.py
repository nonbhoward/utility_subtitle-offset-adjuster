import os
import os.path
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
    for file in working_dir_file_list:
        if str(file.name).endswith(file_extension):
            return file.name


def find_subtitle_file_with_extension(file_extension):
    working_dir_file_list = get_list_of_files_in_dir()
    return filter_subtitle_files(working_dir_file_list, file_extension)


def get_list_of_files_in_dir():
    return os.scandir(get_subtitle_dir())


def get_subtitle_dir() -> str:
    return os.getcwd()


def load_subtitle_file(filename: str):
    loaded_file = open(filename, "r")
    # debug # print(read_file_contents(loaded_file))
    # debug # print(read_file_contents_by_line(loaded_file, line_number=15))
    print(read_file_contents_by_line_range(loaded_file, line_start=15, line_end=25))
    return loaded_file


def read_file_contents(loaded_file):
    loaded_file_contents = loaded_file.read()
    return loaded_file_contents


def read_file_contents_by_line(loaded_file, line_number: int):
    loaded_file_line = loaded_file.readlines(line_number)
    return loaded_file_line


def read_file_contents_by_line_range(loaded_file, line_start: int, line_end: int):
    loaded_file_line_range = loaded_file
    for _ in range(line_start, line_end):
        print(_)
    return loaded_file_line_range


def set_subtitle_extension(file_extension):
    return file_extension  # fixme this makes no sense in current structure


def set_subtitle_dir(dir_path: str):
    os.chdir(dir_path)


# meta-code notes
# dev-complete : set/get a working directory @get_subtitle_dir()
# dev-future : browse-able directory selector?
# dev-complete : get a list of all files in active dir @find_subtitle_file()
# dev-complete : filter the list to the relevant subtitle files ".srt"
# dev-future : handle dirs with more than one subtitle file
# dev-complete : print all contents from the selected text file
# dev-complete : print a selected line number from the selected text file
# dev-in-progress : print a selected line range from the selected text file
# dev-future : present a selectable input if more than one available file
# dev-future : present the option to shift subtitle forward or back in time
# dev-in-progress : present the option to input an integer time shift
# dev-future : present the option to input a decimal time shift
sub_file = Subtitle(".srt")
sub_ext = sub_file.get_file_extension()
print("The active subtitle file is : " + str(sub_ext))
load_subtitle_file(find_subtitle_file_with_extension(sub_ext))

# end

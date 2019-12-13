import os
import os.path
import shutil
import pathlib
import string


def filter_subtitle_files(file_list, file_extension):
    for file in file_list:
        if str(file.name).endswith(file_extension):
            return file.name


def find_subtitle_file():
    file_extension = set_subtitle_extension(".srt")
    working_dir_file_list = get_list_of_files_in_dir()
    return filter_subtitle_files(working_dir_file_list, file_extension)


def get_list_of_files_in_dir():
    return os.scandir(get_subtitle_dir())


def get_subtitle_dir() -> str:
    return os.getcwd()


def load_subtitle_file(filename: str):
    subtitle_file_to_edit = open(filename, "r")
    print(subtitle_file_to_edit.read())


def set_subtitle_extension(file_extension):
    return file_extension


def set_subtitle_dir(dir_path: str):
    os.chdir(dir_path)


# meta-code & notes
# set/get a working directory @get_subtitle_dir()
# get a list of all files @find_subtitle_file()
# filter the list to the relevant subtitle files ".srt"
subtitle_file = find_subtitle_file()
print("The subtitle file being operated on is : " + str(subtitle_file))
load_subtitle_file(subtitle_file)
# option : present a selectable input if more than one available file
# option : present the option to shift subtitle forward or back in time
# present the option to input an integer time shift
# option : present the option to input a decimal time shift

# end

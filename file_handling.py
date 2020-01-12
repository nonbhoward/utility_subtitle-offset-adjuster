from Subtitle import *
from os_check import *
import pathlib, os


def filter_subtitle_files(working_dir_file_list: list, file_extension: str) -> str:
    sub_file = Subtitle(file_extension, filename="")
    for file in working_dir_file_list:
        # iterate over files in cwd, use str.lower() for comparison
        if str(file).lower().endswith(sub_file.get_file_extension()):
            return str(file)


def find_subtitle_file(file_extension) -> list:  # todo cwd limitation is restrictive
    working_dir = os.getcwd()  # get current working directory aka 'cwd'
    working_dir_file_list = os.listdir(working_dir)  # get list() of files in cwd
    return filter_subtitle_files(working_dir_file_list, file_extension)


def open_subtitle_file(filename: list) -> list:
    sub_file = pathlib.Path(filename)
    print("Debug : Started reading from filename : " + str(filename))
    # debug # file_contents = read_file_contents(filename)
    file_contents = read_file_contents_as_list(filename)
    return file_contents


def read_file_contents_as_list(filename: str) -> list:
    try:
        with open(filename, "r") as loaded_file:
            return loaded_file.readlines()
    except FileNotFoundError as error_FNF:
        print(error_FNF)





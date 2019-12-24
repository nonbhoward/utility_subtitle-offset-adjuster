from Subtitle import *
import pathlib


def filter_subtitle_files(working_dir_file_list, file_extension) -> str:
    sub_file = Subtitle(file_extension, filename="")
    for file in working_dir_file_list:
        if str(file.name).endswith(sub_file.get_file_extension()):
            return file.name


def find_subtitle_file(file_extension) -> str:  # todo cwd limitation is restrictive
    # returns files in cwd according to glob(path, pattern)
    working_dir_file_list = pathlib.Path.glob(pathlib.Path.cwd(), "*")
    return filter_subtitle_files(working_dir_file_list, file_extension)


def open_subtitle_file(filename: str) -> list:
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


def read_file_contents_as_string(filename: str) -> str:
    try:
        with open(filename, "r") as loaded_file:
            return loaded_file.read()
    except FileNotFoundError as error_FNF:
        print(error_FNF)


from Subtitle import *
import pathlib


def filter_subtitle_files(working_dir_file_list, file_extension):
    sub_file = Subtitle(file_extension, filename="")
    for file in working_dir_file_list:
        if str(file.name).endswith(sub_file.get_file_extension()):
            return file.name


def find_subtitle_file(file_extension):  # todo cwd limitation is restrictive
    # returns files in cwd according to glob(path, pattern)
    working_dir_file_list = pathlib.Path.glob(pathlib.Path.cwd(), "*")
    return filter_subtitle_files(working_dir_file_list, file_extension)


def open_subtitle_file(filename: str):
    sub_file = pathlib.Path(filename)
    if sub_file.exists():
        print("Debug : Reading from filename " + str(filename))
        # debug # file_contents = read_file_contents(filename)
        file_contents = read_file_contents_as_list(filename)
        return file_contents
    else:
        print("Debug : File does not exist")
        file_contents = "File contents not found."
        return file_contents


def read_file_contents_as_list(filename: str) -> list:
    with open(filename, "r") as loaded_file:
        return loaded_file.readlines()


def read_file_contents_as_string(filename: str) -> str:
    with open(filename, "r") as loaded_file:
        return loaded_file.read()


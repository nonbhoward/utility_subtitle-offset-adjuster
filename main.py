import os
import os.path
import shutil
import pathlib
import string


def filter_subtitle_files():
    print("todo")


def get_subtitle_dir() -> str:
    dir_path = os.getcwd()
    return dir_path


def list_subtitle_files_only():
    working_dir_file_list = os.scandir(get_subtitle_dir())
    for file in working_dir_file_list:
        print(str(file.name).split('.'))


def load_subtitle_file(filename: str):
    print("todo")


def set_subtitle_dir(dir_path: str):
    os.chdir(dir_path)


list_subtitle_files_only()

# end

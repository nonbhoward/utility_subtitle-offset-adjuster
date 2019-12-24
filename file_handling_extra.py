import pathlib


def read_file_contents_as_string(filename: str) -> str:
    try:
        with open(filename, "r") as loaded_file:
            return loaded_file.read()
    except FileNotFoundError as error_FNF:
        print(error_FNF)
        
        
def read_file_contents_by_line_by_filename(filename, line_number: int):
    version = "for"
    if version == "while":  # todo this works but can be done better
        with open(filename, "r") as loaded_file:
            line = loaded_file.readline()
            line_count = 1
            while line:
                if line_count == line_number:
                    # debug # print("Line {}: {}".format(line_count, line.strip()))
                    return line.format(line_count, line.strip())
                line = loaded_file.readline()
                line_count += 1
    elif version == "for":  # fixme
        with open(filename, "r") as loaded_file:
            for line_count, line in enumerate(loaded_file):
                if line_count == line_number:
                    return "".format(line)


def read_file_contents_by_line_range_by_filename(loaded_file, line_start: int, line_end: int) -> list:
    return None  # todo maybe later if needed


def set_subtitle_dir(dir_path: str):  # todo return type?  # todo untested function
    # is this better? # os.chdir(dir_path)
    cwd_path = pathlib.Path(dir_path)
    pathlib.Path(cwd_path)

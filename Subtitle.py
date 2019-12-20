class Subtitle:
    def __init__(self, file_extension: str, filename: str):
        self.file_extension = ".srt"
        self.filename = None

    def get_file_extension(self):
        return self.file_extension

    def get_filename(self):
        return self.filename

    def set_file_extension(self, new_file_extension):
        self.file_extension = new_file_extension

    def set_filename(self, new_filename):
        self.filename = new_filename

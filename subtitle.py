class Subtitle:
    def __init__(self, filename=None):
        self.file_extension = ".srt"
        self.filename = filename

    def get_file_extension(self) -> str:
        return self.file_extension

    def get_filename(self) -> str:
        return self.filename

    def set_file_extension(self, new_file_extension):
        self.file_extension = new_file_extension

    def set_filename(self, new_filename):
        self.filename = new_filename

class Subtitle:
    def __init__(self, filename=None):
        self.file_extension = ".srt"
        self.filename = filename
        self.time_shift = 0

    def generate_output_filename(self):
        self.output_filename = self.get_filename_without_extension() + "_shifted.srt"

    def get_file_extension(self) -> str:
        return self.file_extension

    def get_filename(self) -> str:
        return self.filename

    def get_filename_without_extension(self) -> str:
        return self.filename.rstrip(".srt")

    def set_file_extension(self, new_file_extension):
        self.file_extension = new_file_extension

    def set_filename(self, new_filename):
        self.filename = new_filename

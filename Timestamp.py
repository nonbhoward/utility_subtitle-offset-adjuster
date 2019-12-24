class Timestamp:
    def __init__(self, format_string: str):
        self.format_string = format_string

    def get_format(self) -> str:
        return self.format_string

    def set_format(self, new_format_string) -> str:
        self.format_string = new_format_string

# i may use this, i may not

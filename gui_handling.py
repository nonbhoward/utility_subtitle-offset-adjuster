import PySimpleGUI as pgui
import sys


class Interface:
    def __init__(self, interface_name):
        self.state = "Fetch Subtitle"
        self.interface_name = interface_name
        self.location = self.get_window_location()
        self.layout = self.get_layout_to_fetch_subtitle_file()
        self.window = self.get_window()

    def button_get_size_big(self):
        width, height = 40, 10
        return (width, height)

    def button_get_size_big_half_height(self):
        width, height = self.button_get_size_big()
        return (width, int(height/2))

    def button_get_size_big_half_width(self):
        width, height = self.button_get_size_big()
        return (int(width/2), height)

    def button_get_cancel(self):
        big_cancel_button = pgui.Button(button_text="Cancel",
                                        tooltip="Cancel",
                                        size=self.button_get_size_big_half_height())
        return big_cancel_button

    def button_get_filebrowse_srt(self):
        return pgui.FileBrowse("Browse",
                               file_types=(('Subtitle files', '*.srt'),),
                               size=self.button_get_size_big())

    def button_get_filebrowse_experimental(self):
        filebrowse_button = pgui.Button(button_text="Browse",
                                        tooltip="Browse to the subtitle!",
                                        file_types=(('Subtitle files', '*.srt'),),
                                        initial_folder="~/",
                                        size=self.button_get_size_big())
        return filebrowse_button

    def button_get_select(self):
        select_button = pgui.Button(button_text="Select",
                                    size=self.button_get_size_big_half_height())
        return select_button

    def display_get_input_text(self):
        input_text = pgui.Input(default_text="No subtitle selected")
        return input_text

    def get_layout(self):
        if self.state == "Fetch Subtitle":
            self.get_layout_to_fetch_subtitle_file()
        else:
            sys.exit()

    def get_layout_to_fetch_subtitle_file(self):
        return [[self.text_get_subtitle_prompt()],
                [self.display_get_input_text()],
                [self.button_get_filebrowse_srt()],
                [self.button_get_select()],
                [self.button_get_cancel()]]

    def get_window(self):
        window = pgui.Window(title=self.interface_name,
                             layout=self.layout,
                             location=self.location)
        return window

    def get_window_location(self):
        return (2500, 2500)  # center of bottom right monitor in reverse L configuration

    def launch_interface_to_get_subtitle_file(self):
        if len(sys.argv) == 1:
            event, values = pgui.Window('Locate Subtitle File',
                                        [[pgui.Text('Subtitle to open')],
                                         [pgui.In(), pgui.FileBrowse(file_types=(('Subtitle files', '*.srt'),),
                                                                     size=self.button_get_size_big())],
                                         [pgui.Open(), pgui.Cancel()]],
                                        location=self.get_window_location()).read(close=True)
            sub_filename = values[0]
        else:
            sub_filename = sys.argv[1]

        if not sub_filename:
            raise SystemExit('cancel, no file selected')
        else:
            pgui.popup('the subtitle file chosen is', sub_filename, location=self.get_window_location())

    def text_get_subtitle_prompt(self):
        subtitle_prompt = pgui.Text(text="Locate subtitle file",
                                    size=(40, 2))
        return subtitle_prompt


if __name__ == '__main__':
    test_gui = Interface("Subtitle Offset Adjustment")
    test_gui.launch_interface_to_get_subtitle_file()

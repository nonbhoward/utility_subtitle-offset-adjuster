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
        return (40, 10)

    def button_get_cancel_big(self):
        big_cancel_button = pgui.Button(button_text="Cancel",
                                        tooltip="Cancel",
                                        size=(40, 5))
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

    def get_layout(self):
        if self.state == "Fetch Subtitle":
            self.get_layout_to_fetch_subtitle_file()
        else:
            sys.exit()

    def get_layout_to_fetch_subtitle_file(self):
        return [[self.text_get_subtitle_prompt()], [self.button_get_filebrowse_srt()], [self.button_get_cancel_big()]]

    def get_window(self):
        return pgui.Window(self.interface_name, layout=self.layout, location=self.location)

    def get_window_location(self):
        return (2500, 2500)  # center of bottom right monitor in reverse L configuration

    def launch_interface_to_get_subtitle_file(self):
        while True:
            event, values = self.window.read()
            if event == "Cancel" or event == pgui.WIN_CLOSED:
                break
        self.window.close()

    def text_get_subtitle_prompt(self):
        subtitle_prompt = pgui.Text(text="Locate subtitle file",
                                    size=(40, 2))
        return subtitle_prompt


if __name__ == '__main__':
    test_gui = Interface("Subtitle Offset Adjustment")
    test_gui.launch_interface_to_get_subtitle_file()

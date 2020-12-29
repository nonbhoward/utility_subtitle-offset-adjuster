from minimalog.minimal_log import MinimalLog
import PySimpleGUI as pgui
import sys
mlog = MinimalLog(__name__)


class Interface:
    def __init__(self, interface_name):
        init_event = 'initializing Interface object'
        mlog.log_event(init_event, event_completed=False)
        self.state = "Fetch Subtitle"
        self.interface_name = interface_name
        self.location = self.get_window_location()
        self.layout = self.get_layout_to_fetch_subtitle_file()
        self.window = self.get_window()
        mlog.log_event(init_event, event_completed=True)

    def button_get_size_big(self):
        width, height = 40, 10
        return width, height

    def button_get_size_big_half_height(self):
        width, height = self.button_get_size_big()
        return width, int(height/2)

    def button_get_size_big_half_width(self):
        width, height = self.button_get_size_big()
        return int(width/2), height

    def button_get_cancel(self):
        build_event = 'building cancel button object'
        mlog.log_event(build_event, event_completed=False)
        big_cancel_button = pgui.Button(button_text="Cancel",
                                        tooltip="Cancel",
                                        size=self.button_get_size_big_half_height())
        mlog.log_event(build_event, event_completed=True)
        return big_cancel_button

    def button_get_filebrowse_srt(self):
        build_event = 'building file browse srt button object'
        mlog.log_event(build_event, event_completed=False)
        file_browse_button = pgui.FileBrowse("Browse",
                                             file_types=(('Subtitle files', '*.srt'),),
                                             size=self.button_get_size_big())
        mlog.log_event(build_event, event_completed=True)
        return file_browse_button

    def button_get_filebrowse_experimental(self):
        build_event = 'building file browse button object, experimental'
        mlog.log_event(build_event, event_completed=False)
        filebrowse_button = pgui.Button(button_text="Browse",
                                        tooltip="Browse to the subtitle!",
                                        file_types=(('Subtitle files', '*.srt'),),
                                        initial_folder="~/",
                                        size=self.button_get_size_big())
        mlog.log_event(build_event, event_completed=True)
        return filebrowse_button

    def button_get_select(self):
        build_event = 'building select button object'
        mlog.log_event(build_event, event_completed=False)
        select_button = pgui.Button(button_text="Select",
                                    size=self.button_get_size_big_half_height())
        mlog.log_event(build_event, event_completed=True)
        return select_button

    def display_get_input_text(self):
        build_event = 'get text to display'
        mlog.log_event(build_event, event_completed=False)
        input_text = pgui.Input(default_text="No subtitle selected")
        mlog.log_event(build_event, event_completed=True)
        return input_text

    def get_layout(self):
        if self.state == "Fetch Subtitle":
            self.get_layout_to_fetch_subtitle_file()
        else:
            sys.exit()

    def get_layout_to_fetch_subtitle_file(self):
        logged_event = 'get interface layout to fetch subtitle'
        mlog.log_event(logged_event, event_completed=False)
        layout = [[self.text_get_subtitle_prompt()],
                  [self.display_get_input_text()],
                  [self.button_get_filebrowse_srt()],
                  [self.button_get_select()],
                  [self.button_get_cancel()]]
        mlog.log_event(logged_event, event_completed=True)
        return layout

    def _get_text(self, text_to_fetch):
        if text_to_fetch == 'Title':
            return 'Subtitle Shifter'
        if text_to_fetch == 'Subtitle Window Instructions':
            return 'Select subtitle file and a positive integer timeshift between 1 and 59'

    def get_window(self):
        build_event = 'getting window object'
        mlog.log_event(build_event, event_completed=False)
        window = pgui.Window(title=self.interface_name,
                             layout=self.layout,
                             location=self.location)
        mlog.log_event(build_event, event_completed=True)
        return window

    def get_window_location(self):
        return (2500, 2500)  # center of bottom right monitor in reverse L configuration

    def launch_interface_to_get_subtitle_file(self):
        action_event = 'launching interface to fetch subtitle'
        mlog.log_event(action_event, event_completed=False)
        if len(sys.argv) == 1:
            trigger_event = 'monitoring window object'
            mlog.log_event(trigger_event, event_completed=False)
            event, values = pgui.Window(self._get_text("Title"),
                                        [[pgui.Text(self._get_text("Subtitle Window Instructions"))],
                                         [pgui.In(), pgui.FileBrowse(file_types=(('Subtitle files', '*.srt'),),)],
                                         [pgui.In(), pgui.Text("Offset integer")],
                                         [pgui.Open(), pgui.Cancel()]],
                                        location=self.get_window_location()).read(close=True)
            value_event = 'fetching values from interface'
            mlog.log_event(value_event, event_completed=False)
            sub_filename, seconds_offset = values[0], values[1]
            if event == "Cancel" or pgui.WINDOW_CLOSED:
                cancel_event = 'cancel button selected, exiting program'
                mlog.log_event(cancel_event)
                sys.exit()
            if sub_filename and seconds_offset:
                seconds_offset = int(seconds_offset)
                mlog.log_event(value_event, event_completed=True)
            else:
                self.launch_interface_to_get_subtitle_file()
        else:
            warn_event = 'unable to fetch seconds_offset'
            mlog.log_event(warn_event, level=mlog.WARN)
            sub_filename = sys.argv[1]
            seconds_offset = 0

        if not sub_filename or not isinstance(seconds_offset, int):
            raise SystemExit('cancel, no file selected or offset not integer')
        else:
            return sub_filename, seconds_offset

    def text_get_subtitle_prompt(self):
        build_event = 'get text display for subtitle prompt'
        mlog.log_event(build_event, event_completed=False)
        subtitle_prompt = pgui.Text(text="Locate subtitle file",
                                    size=(40, 2))
        mlog.log_event(build_event, event_completed=True)
        return subtitle_prompt


if __name__ == '__main__':
    main_event = 'executing gui_handling module directly'
    mlog.log_event(main_event)
    test_gui = Interface("Subtitle Offset Adjustment")
    test_gui.launch_interface_to_get_subtitle_file()
    mlog.log_event(main_event, event_completed=True)

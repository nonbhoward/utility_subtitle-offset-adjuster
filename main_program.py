from handler_functions.file_handling import open_subtitle_file
from handler_functions.gui_handling import Interface
from handler_functions.line_handling import build_shifted_subtitle
from handler_functions.time_handling import get_datetime_timeshift
from subtitle_class import Subtitle

interface = Interface('Select subtitle file')
sf = Subtitle()
sf.filename, seconds_offset = interface.launch_interface_to_get_subtitle_file()
sf.unshifted = open_subtitle_file(sf.filename)
sf.timeshift = get_datetime_timeshift(hour=0, minute=0, second=seconds_offset)
sf.shifted = build_shifted_subtitle(sf.unshifted, time_shift=sf.timeshift)
sf.generate_output_filename()
with open(sf.output_filename, "w") as f:
    for shifted_line in sf.shifted:
        f.writelines(shifted_line + '\n')
print("Debug : The active subtitle extension is : " + str(sf.file_extension))
print("Debug : Stopped reading from filename : " + str(sf.filename))

# dev-future : present the option to shift subtitle forward or back in time
# dev-in-progress : present the option to input an integer time shift

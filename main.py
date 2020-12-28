from file_handling import find_subtitle_file
from file_handling import open_subtitle_file
from file_handling import Subtitle
from gui_handling import Interface
from line_handling import build_shifted_subtitle
from time_handling import get_datetime_timeshift

interface = Interface('Select subtitle file')
interface.launch_interface_to_get_subtitle_file()
sf = Subtitle()
sf.filename = find_subtitle_file(sf.get_file_extension())
sf.unshifted = open_subtitle_file(sf.filename)
sf.timeshift = get_datetime_timeshift(hour=0, minute=0, second=15.01)
sf.shifted = build_shifted_subtitle(sf.unshifted, time_shift=sf.timeshift)
sf.generate_output_filename()
with open(sf.output_filename, "w") as f:
    for shifted_line in sf.shifted:
        f.writelines(shifted_line + '\n')
print("Debug : The active subtitle extension is : " + str(sf.file_extension))
print("Debug : Stopped reading from filename : " + str(sf.filename))

# dev-future : browse-able directory selector?
# dev-future : handle dirs with more than one subtitle file
# dev-extra : print a selected line range from the selected text file
# dev-future : present a selectable input if more than one available file
# dev-future : present the option to shift subtitle forward or back in time
# dev-in-progress : present the option to input an integer time shift
# dev-future : present the option to input a decimal time shift

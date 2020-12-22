from file_handling import *
from line_handling import *
from time_handling import *

sf = Subtitle()
sf.filename = find_subtitle_file(sf.get_file_extension())
sf.unshifted = open_subtitle_file(sf.filename)
sf.timeshift = get_datetime_timeshift(hour=0, minute=0, second=15.01)
sf.shifted = build_shifted_subtitle(sf.unshifted, time_shift=sf.timeshift)
with open("filename.txt", "w") as f:
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

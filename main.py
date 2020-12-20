from file_handling import *
from line_handling import *

sf = Subtitle()
sf.filename = find_subtitle_file(sf.get_file_extension())
file_contents = open_subtitle_file(sf.filename)
# ... begin construction zone ... #
print(build_shifted_subtitle(file_contents, time_shift=0))
with open("filename.txt", "w") as f:
    print("write some stuff here..")
print("Debug : The active subtitle extension is : " + str(sf.file_extension))
print("Debug : Stopped reading from filename : " + str(sf.filename))

# dev-future : browse-able directory selector?
# dev-future : handle dirs with more than one subtitle file
# dev-extra : print a selected line range from the selected text file
# dev-future : present a selectable input if more than one available file
# dev-future : present the option to shift subtitle forward or back in time
# dev-in-progress : present the option to input an integer time shift
# dev-future : present the option to input a decimal time shift

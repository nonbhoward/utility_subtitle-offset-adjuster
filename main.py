from file_handling import *
from line_handling import *

subtitle_file = Subtitle(".srt", filename="")  # initialize Subtitle() object
file_extension = subtitle_file.get_file_extension()  # assigns the file extension to a variable
subtitle_file.filename = find_subtitle_file(file_extension)  # the file name to be read
file_contents = open_subtitle_file(subtitle_file.filename)  # a list of each read line
# ... begin construction zone ... #
print("Debug : Building shifted timestamp")
print(build_shifted_subtitle(file_contents, time_shift=0))
print("Debug : The active subtitle extension is : " + str(subtitle_file.file_extension))
print("Debug : Stopped reading from filename : " + str(subtitle_file.filename))

# self-notes
# dev-decided : do you want to pass filename strings or handles? filename strings for now
# timeline
# dev-complete : set/get a working directory
# dev-future : browse-able directory selector?
# dev-complete : get a list of all files in active dir
# dev-complete : filter the list to the relevant subtitle files ".srt"
# dev-future : handle dirs with more than one subtitle file
# dev-complete : print all contents from the selected text file
# dev-complete : print a selected line number from the selected text file
# dev-extra : print a selected line range from the selected text file
# dev-future : present a selectable input if more than one available file
# dev-future : present the option to shift subtitle forward or back in time
# dev-in-progress : present the option to input an integer time shift
# dev-future : present the option to input a decimal time shift

# end

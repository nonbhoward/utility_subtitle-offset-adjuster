from file_handling import *
from timestamp_handling import *

# initialize subtitle_file to a Subtitle class object
subtitle_file = Subtitle(".srt", filename="")
file_extension = subtitle_file.get_file_extension()
subtitle_file.filename = find_subtitle_file(file_extension)
file_contents = open_subtitle_file(subtitle_file.filename)
for line_from_file in file_contents:
    if find_timestamp_line(line_from_file) is not None:
        hours_from_line = filter_hours(line_from_file)
        minutes_from_line = filter_minutes(line_from_file)
        seconds_from_line = filter_seconds(line_from_file)
        millis_from_line = filter_milliseconds(line_from_file)
        print(hours_from_line + minutes_from_line + seconds_from_line + millis_from_line)
print("Debug : The active subtitle extension is : " + str(subtitle_file.file_extension))
print("Debug : Reading from the subtitle file : " + str(subtitle_file.filename))

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

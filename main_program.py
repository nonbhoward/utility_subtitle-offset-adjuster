from handler_functions.file_handling import open_subtitle_file
from handler_functions.gui_handling import Interface
from handler_functions.line_handling import build_shifted_subtitle
from handler_functions.time_handling import get_datetime_timeshift
from minimalog.minimal_log import MinimalLog
from subtitle_class import Subtitle
# MinimalLog.clean_up()
mlog = MinimalLog()

interface = Interface('Select subtitle file')
sf = Subtitle()

mlog.log_event('launching interface')
sf.filename, seconds_offset = interface.launch_interface_to_get_subtitle_file()

mlog.log_event('reading unshifted subtitles')
sf.unshifted = open_subtitle_file(sf.filename)

mlog.log_event('converting timeshift to datetime object')
sf.timeshift = get_datetime_timeshift(hour=0, minute=0, second=seconds_offset)

mlog.log_event('building shifted subtitles')
sf.shifted = build_shifted_subtitle(sf.unshifted, time_shift=sf.timeshift)
sf.generate_output_filename()

subtitle_write_event = 'writing shifted timestamps to subtitle'
mlog.log_event(subtitle_write_event, event_completed=False)
with open(sf.output_filename, "w") as f:
    for shifted_line in sf.shifted:
        f.writelines(shifted_line + '\n')
mlog.log_event(subtitle_write_event, event_completed=True)

# dev-future : present the option to shift subtitle forward or back in time

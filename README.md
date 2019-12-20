# utility_subtitle-offset-adjust

This project is a text parser that will 

01. Parse text subtitle files with timestamp line format:

00:00:00,000 --> 00:00:00,000

Note: The regex in the program could easily be adjusted to parse other subtitle timestamp formats, this is just the format of the file with which I was working at the time

02. Timeshift those timestamp lines by any number of minutes, seconds, or milliseconds and produce a new file



I just finished parsing in the hours, minutes, seconds, and milliseconds as lists of strings so I'll be starting on the math functions as soon as I get some time

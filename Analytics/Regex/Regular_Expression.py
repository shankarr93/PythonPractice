import pandas as pd
import re

#To read input CSV file using pandas
ufo = pd.read_csv('https://raw.githubusercontent.com/shankarr93/PythonPractice/master/Analytics/Regex/ufo-scrubbed-geocoded-time-standardized.csv', header=None)

#Durations Column is copied to the variable durations.
durations = ufo[6].tolist()

#Below are the regex patterns to get details of various time formats
pattern_number = re.compile(r'[\d.]+')       # for whole number or a decimal (like '20' or '4.5')
pattern_fraction = re.compile(r'(\d+)/(\d+)')    # for a fraction (like '1/2')
pattern_range = re.compile(r'(\d+)(-| to )(\d+)')    # for a range (like '20-30' or '20 to 30')
pattern_time = re.compile(r'hour|hr|min|sec')    # for a time unit
pattern_substitution = re.compile(r'several|couple|few|one')   # for non number representation
substitutions = {'several': '5', 'couple': '2', 'few': '2', 'one': '1'}  #for words like several, couple, few, one

clean_durations = []

#The below loop is used to get the matching patterns as compiled above.
#They are appended to list variable clean_durations.
for text in durations:

    # to each pattern and store the resulting match object
    match_number = pattern_number.search(text)
    match_fraction = pattern_fraction.search(text)
    match_range = pattern_range.search(text)
    match_substitution = pattern_substitution.search(text)
    match_time = pattern_time.search(text)

    if match_range:
        range_start = float(match_range.group(1))
        range_end = float(match_range.group(3))
        number = str((range_start + range_end) / 2)

    elif match_fraction:
        numerator = float(match_fraction.group(1))
        denominator = float(match_fraction.group(2))
        number = str(numerator / denominator)

    elif match_number:
        number = match_number.group()

    elif match_substitution:
        number = substitutions[match_substitution.group()]

    else:
        number = 'not found'

    if match_time:
        time = match_time.group()
        standard_time = re.sub(r'hour', r'hr', time)
    else:
        standard_time = 'not found'

    clean_durations.append((text, number, standard_time))

print('Please find the clean Durations of CSV file below:')
print(clean_durations)

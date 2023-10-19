import random
import time
from datetime import datetime

def generate_unix_timestamp():
    # Generate a random Unix timestamp between January 1, 2010, and December 31, 2020
    start_timestamp = time.mktime(datetime(2010, 1, 1).timetuple())
    end_timestamp = time.mktime(datetime(2020, 12, 31).timetuple())
    random_timestamp = int(time.mktime(datetime.fromtimestamp(start_timestamp + (end_timestamp - start_timestamp) * random.random()).timetuple()))
    return str(random_timestamp)

def process_line(line):
    # Format each line to the specified format
    formatted_line = f'{{"text":"{line.strip()}","utc":"{generate_unix_timestamp()}"}}'
    return formatted_line

# Specify the input and output file paths
input_file_path = 'corpusSkills.txt'
output_file_path = 'corpusSkills.jsonl'

# Process each line and write to the output file
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        formatted_line = process_line(line)
        output_file.write(formatted_line + '\n')

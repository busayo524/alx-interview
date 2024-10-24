0x03. Log Parsing
Overview

This project is focused on building a Log Parsing system in Python, where you'll process incoming data streams and compute useful metrics in real-time. You will practice Python file I/O, signal handling, regular expressions, and data processing techniques, all while working with dictionaries to aggregate data. The goal is to handle log data efficiently and produce statistical summaries based on incoming log entries.
Requirements
General

    Allowed editors: vi, vim, emacs
    Files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
    Code should follow the PEP 8 style guide (version 1.7.x).
    Files must end with a new line and be executable.
    The first line of each file must be #!/usr/bin/python3.
    README.md is mandatory.
    File lengths will be tested using the wc command.

Concepts Covered

    File I/O in Python: Reading from sys.stdin line by line.
    Signal Handling: Managing keyboard interruptions (CTRL + C) to gracefully terminate processes.
    Data Processing: Parsing and extracting data from log entries.
    Regular Expressions: Validating the format of incoming data.
    Dictionaries: Storing and counting occurrences of status codes and file sizes.
    Exception Handling: Safely handling unexpected errors during data processing.

Task: Log Parsing
Script Overview

You need to write a script that:

    Reads log data line by line from stdin.
    For every 10 lines, or when the program is interrupted (CTRL + C), prints the following metrics:
        Total file size: The sum of all file sizes processed.
        Status code counts: The number of occurrences of each status code (only for the codes 200, 301, 400, 401, 403, 404, 405, 500).

Input Format

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Example log entry:

10.0.0.1 - [2024-10-21 14:12:45] "GET /projects/260 HTTP/1.1" 200 1024

Output

After every 10 lines and/or on interruption:
Total file size: File size: <total size>
Number of lines by status code (in ascending order):

<status code>: <number>

Example Usage

alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3

Key Notes:

    Only print status codes that have been encountered.
    The program should handle KeyboardInterrupt and print the final statistics before exiting.
    Logs that do not match the required format should be skipped.

Project Timeline

    Start Date: October 21, 2024, 6:00 AM
    End Date: October 25, 2024, 6:00 AM
    Checker Release: October 22, 2024, 6:00 AM
    An auto-review will be performed at the project deadline.

Mock Technical Interview

To help you prepare for technical interviews, there is an optional Mock Technical Interview available. It’s highly recommended to practice for real-world technical scenarios.

#!/usr/bin/python3
"""
Log parsing script
Reads from standard input and computes metrics:
- Total file size from all lines
- Count of each status code
"""
import sys

# Initialize variables
total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

def print_stats():
    """Prints the accumulated metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        try:
            # Extract the file size and status code
            file_size = int(parts[-1])
            status_code = parts[-2]

            # Update total size and status code count
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (IndexError, ValueError):
            # If line format is invalid, skip it
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle CTRL + C (keyboard interrupt)
    print_stats()
    raise

# Final print after processing all lines
print_stats()

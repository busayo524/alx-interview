#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':
    # Initialize the total file size and line counter
    total_filesize, line_count = 0, 0
    # List of valid status codes
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    # Dictionary to track the count of each status code
    status_counts = {code: 0 for code in valid_codes}

    def print_stats(stats: dict, total_size: int) -> None:
        """Prints the accumulated statistics."""
        print("File size: {:d}".format(total_size))
        for key, value in sorted(stats.items()):
            if value > 0:
                print("{}: {}".format(key, value))

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()

            # Update the file size if the value exists
            try:
                total_filesize += int(data[-1])
            except (IndexError, ValueError):
                pass

            # Update the status code count if it's valid
            try:
                status_code = data[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except IndexError:
                pass

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(status_counts, total_filesize)

        # Final stats after reading all lines
        print_stats(status_counts, total_filesize)

    except KeyboardInterrupt:
        # Print stats on keyboard interrupt
        print_stats(status_counts, total_filesize)
        raise

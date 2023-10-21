#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""


import re
import sys


# Initialize variables to store statistics
size = 0
num_lines = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
                "405": 0, "500": 0}
pattern = (
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} .*)\]'
    r' "GET /projects/260 HTTP/1\.1"\s(200|301|[4-5]\d{2}) (\d+)'
)


try:
    for input_str in sys.stdin:
        re_match = re.match(pattern, input_str)
        if re_match:
            num_lines += 1
            size += int(re_match.group(4))
            status_codes[re_match.group(3)] += 1
            if num_lines % 10 == 0:
                print("File size: {}".format(size))
                for key, value in sorted(status_codes.items()):
                    if value > 0:
                        print("{}: {}".format(key, value))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print("{}: {}".format(key, value))

#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == "__main__":
    test_function = __import__("0-subs").number_of_subscribers
    print("{:d}".format(test_function(sys.argv[1])))

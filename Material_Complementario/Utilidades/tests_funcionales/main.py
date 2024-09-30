from utils import cli
#import os, sys, subprocess

prog_info = cli.get_args()

# Test getter
test = prog_info.get_test()

print(f"Input: {test.input}")
print(f"Output: {test.output}")

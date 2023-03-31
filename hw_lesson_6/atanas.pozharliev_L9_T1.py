import sys

file_input = sys.argv[1]
file_output = sys.argv[2]

with open(file_input, "r+") as f:
    lines = f.readlines()

lines.sort()

with open(file_output, "w+") as f:
    f.writelines(lines)

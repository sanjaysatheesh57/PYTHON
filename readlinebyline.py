filename = "sample.txt"     # replace with your file name
lines_list = []             # empty list to store lines

with open(filename, "r") as file:
    for line in file:
        lines_list.append(line.strip())   # strip() removes newline

print("Lines in the list:")
print(lines_list)

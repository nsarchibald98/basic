
# Reads whole txt file.
def read_all(file):
    txt = open(file)
    print(txt.read())


# Read the first line. readline() defaults to read the first line.
def read_first_line(file):
    txt = open(file)
    print(txt.readline())


# Append text to the txt file
def append_txt(file):
    with open(file, 'w') as f:
        f.write('Hello world \n')
        f.write('End of entry')
    txt = open(file)
    print(txt.read())


# Reads the last line
def last_line(file):
    with open(file, 'r') as f:
        for line in f:
            pass
        last = line
    print(last)


last_line('sample3.txt')
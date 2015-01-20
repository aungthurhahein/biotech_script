#file reader template
#23/9/2014
#__author__ = 'atrx'
# just a container to reuse for sytstem without argparse module

from sys import argv
import time

def main(script,filename):
    print("Opening the file")
    file_read = open(filename)
    #code
    loop_by_line(file_read)
    #code
    file_read.close()
    print("Done Reading file")

# function to call
def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

def loop_by_line(f):
    for i in f:
        print i
        time.sleep(3)



if __name__ == "__main__":
    script,filename = argv
    main(script,filename)




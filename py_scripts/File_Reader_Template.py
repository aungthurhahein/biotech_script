#file reader template
#23/9/2014
#__author__ = 'atrx'
# just a container to reuse for sytstem without argparse module

from sys import argv

def main(script,filename):
    print("Opening the file")
    file_read = open(filename)



    #code
    print_all(file_read)
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
        f.readline()



if __name__ == "__main__":
    script,filename = argv
    main(script,filename)



#!/usr/bin/env python
"""
#-------------------------------------------------------------------------#
#To retrive cluster distribution of cd-hit output .clsr file
#Usage
# $ cd_hit_clstr_stat.py xxx.clstr
#Dev: Aung
#Time: 22/10/2014
#-------------------------------------------------------------------------#
"""
import os
import os.path
import argparse

def ParseCommandLine():
    parser = argparse.ArgumentParser('parse cd-hit cluster file and output the cluster member count and summary')
    parser.add_argument('-i', '--input', type= ValidateFileRead,required=True,help="input cluster (.clstr)file from cd-hit-est")
    theargs = parser.parse_args()
    return theargs

def ValidateFileRead(theFile):

    # Validate the path is a valid
    if not os.path.exists(theFile):
        raise argparse.ArgumentTypeError('File does not exist')

    # Validate the path is readable
    if os.access(theFile, os.R_OK):
        return theFile
    else:
        raise argparse.ArgumentTypeError('File is not readable')

def main(input):

    # check input file
    try:
        inputfile=open(input,"rb")
    except:
        p.Print ("file not given...")
        exit(0)

    count = 0
    clstname = ''
    clstrdic={}

    # loop file and count
    for line in inputfile:
        if ">Cluster" in line:
            clstrdic[str(clstname).strip()] = count
            count = 0
            clstname = line
        else:
            count = count+1
    else:
        clstrdic[str(clstname).strip()] = count

    # remove dummy first entry
    del clstrdic['']

    # print the sorted cluster size by member count
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    count8=0

    for key, value in sorted(clstrdic.iteritems(), key=lambda (k,v): (v,k)):
        print "%s: %s" % (key, value)

        if value == 1:
            count1 = count1+1
        elif(value >1 and value <=5):
            count2 = count2+1
        elif(value >5 and value <=10):
            count3= count3+1
        elif(value >10 and value <=20):
            count4= count4+1
        elif(value >20 and value <=40):
            count5= count5+1
        elif(value >40 and value <=80):
            count6= count6+1
        elif(value >80 and value <=100):
            count7= count7+1
        else:
            count8= count8+1
    print""
    print"Summary statistics"
    print "Member without similar sequences:", count1
    print "1>Member<5", count2
    print "5=>Member<10", count3
    print "10=>Member<20"  , count4
    print "20=>Member<40"  , count5
    print "40=>Member<80"  , count6
    print "80=>Member<100"  , count7
    print "Member>100"  , count8


if __name__ == "__main__":
    args = ParseCommandLine()
    main(args.input)

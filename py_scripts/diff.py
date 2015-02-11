import sys

file1= sys.argv[1]#not in
file2= sys.argv[2]#in

read1 = open(file1,'r')
read2 = open(file2,'r')
r1=[];

for i in read1:
  r1.append(i.strip())
#loop second file
for x in read2:
  #loop in first file
  if x.strip() not in r1:
    print x.strip()






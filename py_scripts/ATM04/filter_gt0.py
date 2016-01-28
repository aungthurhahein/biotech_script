#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
mapfile = sys.argv[1]
gt0file = sys.argv[2]

atmid = []
cap3id = []
with open(mapfile,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        atmid.append(l2_split[1].strip())
        cap3id.append(l2_split[2].strip('>\n'))

with open(gt0file,'rb') as f3:    
    for l3 in f3:
        tmpid = []    
        l3_split = l3.split('\t')        
        for m in l3_split[6].split(';'):
            if m.strip('-XN\n') not in atmid:            
                tmpid.append(m.strip('\n'))         
        for m2 in l3_split[6].split(';'):
                tmpcdf = []
                if m2.strip('-XN\n') in atmid:            
                    ind = atmid.index(m2.strip('-XN\n'))                
                    indexes = [i for i,e in enumerate(cap3id) if e == cap3id[ind]]
                    for i in indexes:
                        tmpcdf.append(atmid[i])
                    for m3 in l3_split[6].split(';'):
                        if m3.strip('-XN\n') in tmpcdf:
                            tmpcdf.remove(m3.strip('-XN\n'))
                    if len(tmpcdf) == 0:
                        tmpid.append(cap3id[ind]+"-"+m2.split('-')[1].strip('\n'))
                    # print "*",tmpcdf,m2                    
        uniqtmpid = list(set(tmpid))
        tmpout = "-"
        xcount = 0
        ncount = 0
        for x in uniqtmpid:
            if "-X" in x:
                xcount +=1
            elif "-N" in x:
                ncount +=1
            if tmpout =="-":
                tmpout = x
            else:
                tmpout += ";"+x                
        # print tmpout
        final_fmt = ""
        for out in l3_split[:2]:
            if final_fmt =="":
                final_fmt = out
            else:
                final_fmt +="\t"+out                
        if xcount == ncount == 0:
            total = 0
        else:
            total = len(tmpout.split(';'))
        sys.stdout.write(final_fmt+"\t"+str(total)+"\t"+str(ncount)+'\t'+str(xcount)+"\t"+tmpout+'\n')
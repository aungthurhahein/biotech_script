#! /usr/bin/env/ python
"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
import re
descfile = sys.argv[1]

o1 = open(descfile+"_y",'w')
o2 = open(descfile+"_n",'w')
with open(descfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        clstid = l1_split[0]
        memid = l1_split[1]
        desc = l1_split[2]
        oldclstid = l1_split[3].strip('\n')
        ok = 0
        print clstid
        for m in desc.split('|'):
            m_ = m.strip()
            pro = re.match(r'UPF\d+\sprotein',m_)
            zgc = re.match(r'Zgc:\d+',m_)
            acyp = re.match(r'ACYPI\d+\sprotein',m_)
            agap = re.match(r'AGAP\d+\-P[A,B,C,D,E,F,G,H,I]\-like\sprotein',m_)
            ensap = re.match(r'ENSANGP\d+\-like',m_)         
            agap2 = re.match(r'AGAP\d+\-PA',m_)
            gdp = re.match(r'G[A-Z]\d+',m_)
            cg = re.match(r'C[A-M]\d+\-P[A,B,C,D,E,F,G,H,I]',m_)
            aael = re.match(r'AAEL\d+\-P[A,B,C,D,E,F,G,H,I]',m_)
            protein = re.match(r'[p,P]rotein\s[C,F,B,H]\w+',m_)
            chromo = re.match(r'[c,C]hromosome\s\w+',m_)
            fi = re.match(r'FI\d+p',m_)
            kll = re.match(r'KLLA0F\d+p',m_)
            kllth = re.match(r'KLTH0[D,G]\d+p',m_) 
            ld = re.match(r'LD\d+p',m_) 
            loc = re.match(r'LOC\d+\sprotein',m_) 
            rh = re.match(r'RH\d+p',m_) 
            print m_
            if "Uncharacterized protein" in m_ or\
                "Putative uncharacterized protein" in m_ or\
                "hypothetical protein" in m_ or\
                "conserved hypothetical protein" in m_ or\
                "NaN" in m_ or\
                "Albugo candida WGS project CAIX00000000 data" in m_ or\
                "Unnamed product" in m_ or\
                "Oncorhynchus" in m_ or\
                "Predicted protein" in m_ or\
                "predicted protein" in m_:
                print "OK:0"
            elif pro or zgc or acyp or agap  or ensap or agap2 or gdp or cg or aael or protein or chromo or fi or kll or kllth or ld or loc or rh:
                print pro, zgc, acyp, agap,gdp,cg,aael
                print "OK:0.5"
            else:
                print "OK:1"
                ok = 1
        print ok
        if ok == 1:
            o1.write(l1)
        else:
            o2.write(l1)

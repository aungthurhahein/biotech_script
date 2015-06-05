#!/bin/bash
base='/home/aung/github_repos/biotech_script/py_scripts/'
python $base/ncbi_batch.py -term "Penaeus Monodon AND txid6687" -db sra  -datetype pdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Litopenaeus vannamei AND txid6689" -db sra  -datetype pdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Litopenaeus setiferus AND txid64468" -db sra  -datetype pdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Fenneropenaeus chinensis AND txid139456" -db sra  -datetype pdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Fenneropenaeus indicus AND txid29960" -db sra  -datetype pdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Marsupenaeus japonicas AND txid27405" -db sra  -datetype pdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Macrobrachium rosenbergii AND txid79674" -db nucleotide  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Cherax quadricarinatus AND txid27406" -db sra  -datetype pdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Pacifastacus leniusculus AND txid6720" -db sra  -datetype pdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Homarus americanus AND txid6706" -db sra  -datetype pdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Scylla olivacea AND txid85551" -db sra  -datetype pdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Scylla paramamosain AND txid85552" -db nuclotide  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Callinectes sapidus AND txid6763" -db sra  -datetype pdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Carcinus maenas AND txid6759" -db nucleotide  -datetype pdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m

#!/bin/bash
base='/home/aung/github_repos/biotech_script/py_scripts/'
python $base/ncbi_batch.py -term "Penaeus Monodon AND txid6687" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Litopenaeus vannamei AND txid6689" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Litopenaeus setiferus AND txid64468" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Fenneropenaeus chinensis AND txid139456" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Fenneropenaeus indicus AND txid29960" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Marsupenaeus japonicas AND txid27405" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Macrobrachium rosenbergii AND txid79674" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Cherax quadricarinatus AND txid27406" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Pacifastacus leniusculus AND txid6720" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Homarus americanus AND txid6706" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Scylla olivacea AND txid85551" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Scylla paramamosain AND txid85552" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Callinectes sapidus AND txid6763" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m
python $base/ncbi_batch.py -term "Carcinus maenas AND txid6759" -db sra  -datetype mdat -mindate 2013/07/05 -maxdate 2015/05
sleep 1m

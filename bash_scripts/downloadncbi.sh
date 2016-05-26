# @Author: aungthurhahein
# @Date:   2016-05-13 15:25:57
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-05-13 16:34:33
# usage: ./script.sh $prefix
while IFS='' read -r line || [[ -n "$line" ]]; do
    prefix=$line
    basepath=" ftp://ftp.ncbi.nlm.nih.gov/genomes/all/"
    slash="/"
    pf1="_feature_table.txt.gz"
    pf2="_genomic.fna.gz"
    pf3="_protein.faa.gz"
    pf4="_genomic.gff.gz"
    pf5="_genomic.gbff.gz"
    pf6="_protein.gpff.gz"
    pf7="_assembly_report.txt"
    pf8="_assembly_stats.txt"
    pf9="README.txt"
    pf10="md5checksums.txt"
    pf11="_wgsmaster.gbff.gz"
    out=".sh"    
    echo "mkdir $prefix" > $prefix$out
    echo "wget --directory-prefix=$prefix $basepath$prefix$slash$prefix$pf1" >> $prefix$out
    echo "wget --directory-prefix=$prefix $basepath$prefix$slash$prefix$pf2" >> $prefix$out
    echo "wget --directory-prefix=$prefix $basepath$prefix$slash$prefix$pf3" >> $prefix$out
    echo "wget --directory-prefix=$prefix $basepath$prefix$slash$prefix$pf4" >> $prefix$out
    echo "wget --directory-prefix=$prefix $basepath$prefix$slash$prefix$pf5" >> $prefix$out
    echo "wget --directory-prefix=$prefix $basepath$prefix$slash$prefix$pf6" >> $prefix$out
    echo "wget --directory-prefix=$prefix $basepath$prefix$slash$prefix$pf7" >> $prefix$out
    echo "wget --directory-prefix=$prefix $basepath$prefix$slash$prefix$pf8" >> $prefix$out
    echo "wget --directory-prefix=$prefix $basepath$prefix$slash$pf9" >> $prefix$out
    echo "wget --directory-prefix=$prefix $basepath$prefix$slash$pf10" >> $prefix$out
    echo "wget --directory-prefix=$prefix $basepath$prefix$slash$prefix$pf11" >> $prefix$out
    echo "./$prefix$out &" >> dl_wrap.sh
done < "$1"
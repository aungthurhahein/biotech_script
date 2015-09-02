#!/bin/sh
#$ -S /bin/bash
#Define name of job
#$ -N TrinotateE
# Run in current working dir
#$ -cwd
#flag to notify when the jod submitted(b) or finished(e) or both(be)
#$ -m e
#email to distribute job status
#$ -M aungthurhahein@gmail.com
# for mutli-thread(parallel) jobs, provide no. of nodes to run(even number make sense)
#$ -pe mpich 1

. /fs/home/card/.bashrc
. /fs/home/card/.bash_profile

# input: Trinotate.sqlite and ID-LengthFile to calculate

mkdir Trinotate_tsv && cd Trinotate_tsv
sqlite_file="../Trinotate.sqlite"
trlenfile="../*.fasta_lngth"

# B2:Transcript with ORF
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from Transcript  join ORF on Transcript.transcript_id = ORF.transcript_id;" > Transcript.tsv

# C1:Blast
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from BLASTDbase;" > Blast.tsv

# BlastX
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from BlastDBase left join Transcript on BlastDbase.TrinityID == Transcript.transcript_id where Transcript.transcript_id is not null;" > BlastX.tsv

# BlastP
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from BLASTDbase left join ORF on BlastDbase.TrinityID == ORF.Orf_id where ORF.Orf_id is not null;" > BlastP.tsv

# Description
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from BLASTDbase left join UniprotIndex on BlastDbase.UniprotSearchString == UniprotIndex.Accession where AttributeType = 'D' and BLASTDbase.TrinityID is not null and UniprotIndex.Accession is not null;" > BlastDescription.tsv

#sqlite3 -header -separator  $'\t' Trinotate.sqlite  "select * from TaxonomyIndex where NCBITaxonomyAccession in (select LinkID from  UniprotIndex where AttributeType == 'T');" > taxonomy.tsv

# GO
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from BLASTDbase left join UniprotIndex on BlastDbase.UniprotSearchString == UniprotIndex.Accession where AttributeType = 'G' and BLASTDbase.TrinityID is not null and UniprotIndex.Accession is not null;" > BlastGo.tsv

#TaxonID
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from BLASTDbase left join UniprotIndex on BlastDbase.UniprotSearchString == UniprotIndex.Accession left join TaxonomyIndex on TaxonomyIndex.NCBITaxonomyAccession == UniprotIndex.LinkId where AttributeType = 'T' and BLASTDbase.TrinityID is not null and UniprotIndex.Accession is not null;" > BlastTaxon.tsv

#eggNOGIndex
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from BLASTDbase left join UniprotIndex on BlastDbase.UniprotSearchString == UniprotIndex.Accession left join eggNOGIndex on eggNOGIndex.EggNOGIndexTerm == UniprotIndex.LinkId where AttributeType = 'E';" > BlastEGGnGI.tsv

# C2:Pfam with Go ID
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from PFAMreference  join pfam2go on pfam_accession = pfam_acc;" > PFamRefGo.tsv

# C3:SignalP
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from SignalP;" > signalp.tsv

# C4:tmhmm
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from tmhmm;" > tmhmm.tsv

# C5: RNammer
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from RNAMMERdata;" > rnammer.tsv

sqlite3 -header -separator  $'\t' $sqlite_file "select BLASTDbase.TrinityID,UniprotIndex.LinkId from RNAMMERdata left join BLASTDbase on RNAMMERdata.TrinityQuerySequence == BLASTDbase.TrinityID left join UniprotIndex on BlastDbase.UniprotSearchString == UniprotIndex.Accession where AttributeType = 'D' and BLASTDbase.TrinityID is not null and UniprotIndex.Accession is not null ;" > rnammer_desc.tsv

cat rnammer_desc.tsv | sort -u > rnammer_desc2.tsv
rm -rf rnammer_desc.tsv
python /fs/home/card/bin/RNammer_Desc.py rnammer_desc2.tsv
rm -rf rnammer_desc2.tsv

# HMMER
 sqlite3 -header -separator  $'\t' $sqlite_file  "select * from HMMERDbase;" > hmmer.tsv

# Get Blast Unique ID for All, BlastP,BlastX
cat Blast.tsv | awk '{print $1}' | sort -u > Blast.uniq.ID
cat BlastP.tsv |awk '{print $1}' | sort -u > BlastP.uniq.ID
cat BlastX.tsv | awk '{print $1}' | sort -u > BlastX.uniq.ID

# Split files based on BlastX or BlastP
python /fs/home/card/bin/xorp.py BlastDescription.tsv $trlenfile
# tophit
perl /fs/home/card/bin/tophit_select.pl BlastDescription.tsv_blastp > BlastDescription.tsv_blastp.tophit
perl /fs/home/card/bin/tophit_select.pl BlastDescription.tsv_blastx > BlastDescription.tsv_blastx.tophit
sed -i '1d' BlastDescription.tsv_blastx.tophit  #remove header from blastx tophit

# tophit <--> Desc
python /fs/home/card/bin/get_blastdesc.py BlastDescription.tsv_blastp.tophit BlastDescription.tsv_blastx.tophit

# others featuers by blast categories

python /fs/home/card/bin/xorp.py BlastGo.tsv $trlenfile
python /fs/home/card/bin/xorp.py BlastTaxon.tsv $trlenfile
python /fs/home/card/bin/xorp.py BlastEGGnGI.tsv $trlenfile


# Debris

#perl /fs/home/card/bin/tophit_select.pl BlastGo.tsv_blastp > BlastGo.tsv_blastp.tophit
#perl /fs/home/card/bin/tophit_select.pl BlastGo.tsv_blastx > BlastGo.tsv_blastx.tophit
#perl /fs/home/card/bin/tophit_select.pl BlastTaxon.tsv_blastp > BlastTaxon.tsv_blastp.tophit
#perl /fs/home/card/bin/tophit_select.pl BlastTaxon.tsv_blastx > BlastTaxon.tsv_blastx.tophit
#perl /fs/home/card/bin/tophit_select.pl BlastEGGnGI.tsv_blastp > BlastEGGnGI.tsv_blastp.tophit
#perl /fs/home/card/bin/tophit_select.pl BlastEGGnGI.tsv_blastx > BlastEGGnGI.tsv_blastx.tophit

# uniportindex with Taxonomy
# sqlite3 -header -separator  $'\t' Trinotate.sqlite  "select * from UniprotIndex left  join TaxonomyIndex on LinkId = NCBITaxonomyAccession where AttributeType == 'T';" > taxonomy.tsv

#sqlite3 -header -separator  $'\t' Trinotate.sqlite  "select * from TaxonomyIndex where NCBITaxonomyAccession in (select LinkID from  UniprotIndex where AttributeType == 'T');" > taxonomy.tsv

# uniportindex with GO
# sqlite3 -header -separator ' ' $sqlite_file  "select * from UniprotIndex  join go on LinkId = id where AttributeType == 'G';" > go.tsv

# uniportindex with EggNo
# sqlite3 -header -separator ' ' $sqlite_file  "select * from UniprotIndex  join eggNOGIndex on LinkId = EggNOGIndexTerm where AttributeType == 'E';" > Eggno.tsv

# uniportindex with Protein Description
# sqlite3 -header -separator ' ' $sqlite_file  "select * from UniprotIndex where AttributeType == 'D';" > Eggno.tsv


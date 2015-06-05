#!/bin/bash
mkdir Trinotate_csv && cd Trinotate_csv
sqlite_file="../Trinotate.sqlite"

# B2:Transcript with ORF
sqlite3 -header -csv $sqlite_file  "select * from Transcript  join ORF on Transcript.transcript_id = ORF.transcript_id;" > Transcript.csv
# C1:Blast
sqlite3 -header -csv $sqlite_file  "select * from BLASTDbase;" > Blast.csv
# C2:Pfam with Go ID
sqlite3 -header -csv $sqlite_file  "select * from PFAMreference  join pfam2go on pfam_accession = pfam_acc;" > PFamRefGo.csv
# C3:SignalP
sqlite3 -header -csv $sqlite_file  "select * from SignalP;" > signalp.csv
# C4:tmhmm
sqlite3 -header -csv $sqlite_file  "select * from tmhmm;" > tmhmm.csv
# C5: RNammer
sqlite3 -header -csv $sqlite_file  "select * from RNAMMERdata;" > rnammer.csv
#HMMER
sqlite3 -header -csv $sqlite_file  "select * from HMMERDbase;" > hmmer.csv
# uniportindex with Taxonomy
sqlite3 -header -csv $sqlite_file  "select * from UniprotIndex  join TaxonomyIndex on LinkId = NCBITaxonomyAccession where AttributeType == 'T';" > taxonomy.csv
# uniportindex with GO
sqlite3 -header -csv $sqlite_file  "select * from UniprotIndex  join go on LinkId = id where AttributeType == 'G';" > go.csv
# uniportindex with EggNo
sqlite3 -header -csv $sqlite_file  "select * from UniprotIndex  join eggNOGIndex on LinkId = EggNOGIndexTerm where AttributeType == 'E';" > Eggno.csv
# uniportindex with Protein Description
sqlite3 -header -csv $sqlite_file  "select * from UniprotIndex where AttributeType == 'D';" > Eggno.csv

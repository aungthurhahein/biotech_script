#!/bin/bash
mkdir Trinotate_tsv && cd Trinotate_tsv
sqlite_file="../Trinotate.sqlite"

# B2:Transcript with ORF
 sqlite3 -header -separator '   ' $sqlite_file  "select * from Transcript  join ORF on Transcript.transcript_id = ORF.transcript_id;" > Transcript.tsv

# C1:Blast
 sqlite3 -header -separator '   ' $sqlite_file  "select * from BLASTDbase;" > Blast.tsv
# BlastX
 sqlite3 -header -separator '   ' $sqlite_file  "select * from Transcript left join BlastDBase on BlastDbase.TrinityID == Transcript.transcript_id where BlastDbase.TrinityID is not null;" > BlastX.tsv
 select * from BlastDBase inner join Transcript on BlastDbase.TrinityID == Transcript.transcript_id inner join UniprotIndex on BlastDbase.UniprotSearchString == UniprotIndex.Accession where Transcript.transcript_id is not null and AttributeType = 'D';
# BlastP
 sqlite3 -header -separator '   ' $sqlite_file  "select * from BLASTDbase left join ORF on BlastDbase.TrinityID == ORF.Orf_id where BlastDbase.TrinityID is not null;" > BlastP.tsv

# Description
 sqlite3 -header -separator '   ' $sqlite_file  "select * from BLASTDbase left join UniprotIndex on BlastDbase.UniprotSearchString == UniprotIndex.Accession where AttributeType = 'D';" > BlastDescription.tsv
# GO
 sqlite3 -header -separator '   ' $sqlite_file  "select * from BLASTDbase left join UniprotIndex on BlastDbase.UniprotSearchString == UniprotIndex.Accession where AttributeType = 'G';" > BlastGo.tsv
#TaxonID
 sqlite3 -header -separator '   ' $sqlite_file  "select * from BLASTDbase left join UniprotIndex on BlastDbase.UniprotSearchString == UniprotIndex.Accession left join TaxonomyIndex on TaxonomyIndex.NCBITaxonomyAccession == UniprotIndex.LinkId where AttributeType = 'T';" > BlastTaxon.tsv
#eggNOGIndex
 sqlite3 -header -separator '   ' $sqlite_file  "select * from BLASTDbase left join UniprotIndex on BlastDbase.UniprotSearchString == UniprotIndex.Accession left join eggNOGIndex on eggNOGIndex.EggNOGIndexTerm == UniprotIndex.LinkId where AttributeType = 'E';" > BlastEGGnGI.tsv

# C2:Pfam with Go ID
 sqlite3 -header -separator '   ' $sqlite_file  "select * from PFAMreference  join pfam2go on pfam_accession = pfam_acc;" > PFamRefGo.tsv

# C3:SignalP
 sqlite3 -header -separator '   ' $sqlite_file  "select * from SignalP;" > signalp.tsv

# C4:tmhmm
 sqlite3 -header -separator '   ' $sqlite_file  "select * from tmhmm;" > tmhmm.tsv

# C5: RNammer
 sqlite3 -header -separator '   ' $sqlite_file  "select * from RNAMMERdata;" > rnammer.tsv

#HMMER
 sqlite3 -header -separator '   ' $sqlite_file  "select * from HMMERDbase;" > hmmer.tsv

# uniportindex with Taxonomy
# sqlite3 -header -separator ' ' $sqlite_file  "select * from UniprotIndex  join TaxonomyIndex on LinkId = NCBITaxonomyAccession where AttributeType == 'T';" > taxonomy.tsv

# uniportindex with GO
# sqlite3 -header -separator ' ' $sqlite_file  "select * from UniprotIndex  join go on LinkId = id where AttributeType == 'G';" > go.tsv

# uniportindex with EggNo
# sqlite3 -header -separator ' ' $sqlite_file  "select * from UniprotIndex  join eggNOGIndex on LinkId = EggNOGIndexTerm where AttributeType == 'E';" > Eggno.tsv

# uniportindex with Protein Description
# sqlite3 -header -separator ' ' $sqlite_file  "select * from UniprotIndex where AttributeType == 'D';" > Eggno.tsv

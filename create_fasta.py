#!/bin/env/python

#takes a fasta string and creates a fasta file using biopython

import Bio.SeqIO
import Bio.Seq
import Bio.SeqRecord

def create_fasta():
    file_seq=open("sequence.txt","r")
    seq=file_seq.read()

    seq_record=Bio.SeqRecord.SeqRecord(Bio.Seq.Seq(seq))
    seq_record.id="sequence"
    with open("sequence.fasta","w") as output_handle:
        Bio.SeqIO.write(seq_record,output_handle,"fasta")
    

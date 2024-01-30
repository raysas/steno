#!/bin/env/python

#takes a fasta string and creates a fasta file using biopython

import Bio.SeqIO

def create_fasta(fasta_string:str, fasta_name:str)->file:
    fasta_file = open(fasta_name, "w")
    
    #use biopython to write the fasta file
    Bio.SeqIO.write(fasta_string, fasta_file, "fasta")

    fasta_file.close()
    return fasta_file

def main():
    #convert a file into a string
    fasta_string = open("CP077679.fasta", "r").read()
    create_fasta(fasta_string, "ref.fasta")

if __name__ == "__main__":
    main()
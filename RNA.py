from rosalind import DNA, RNA

strand_dna = DNA(input())
strand_rna = RNA(strand_dna)
print(strand_rna.strand)
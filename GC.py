import sys
from rosalind import Gene, DNA

doc = "\n".join(sys.stdin.readlines())

strands = Gene.FASTA(doc, DNA)
result = max(strands, key=lambda x: strands[x].GC_content)
print(result, strands[result].GC_content, sep="\n")
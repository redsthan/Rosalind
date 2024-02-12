from collections import Counter

COMPLEMENT = {'A': 'T',
              'C': 'G',
              'G': 'C',
              'T': 'A'}

class DNA:
    def __init__(self, string:str):
        self._strand = string
    
    @property
    def strand(self):
        return self._strand
    
    @property
    def complement(self):
        return "".join([COMPLEMENT[n] for n in reversed(self.strand)])
    
    def count_nt(self):
        occ = Counter(self._strand)
        return [occ[nt] for nt in 'ACGT']
    
    def to_RNA(self):
        return self._strand.replace('T', 'U')
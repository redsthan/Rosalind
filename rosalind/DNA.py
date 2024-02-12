from collections import Counter

class DNA:
    def __init__(self, string:str):
        self._strand = string
    
    @property
    def strand(self):
        return self._strand
    
    def count_nt(self):
        occ = Counter(self._strand)
        return [occ[nt] for nt in 'ACGT']
    
    def to_RNA(self):
        return self._strand.replace('T', 'U')
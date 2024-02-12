from collections import Counter

COMPLEMENT = {'A': 'T',
              'C': 'G',
              'G': 'C',
              'T': 'A'}

class DNA:
    def __init__(self, string:str):
        self._strand = string
        
    def __len__(self):
        return len(self.strand)
    
    def __repr__(self):
        return f"DNA({self.strand})"
    
    @property
    def strand(self):
        return self._strand
    
    @property
    def complement(self):
        return "".join([COMPLEMENT[n] for n in reversed(self.strand)])
    
    @property
    def GC_content(self):
        A, C, G, T = self.count_nt()
        return ((C+G)/len(self))*100
    
    @property
    def AT_content(self):
        return 100-self.GC_content
    
    def count_nt(self):
        occ = Counter(self._strand)
        return [occ[nt] for nt in 'ACGT']
    
    def to_RNA(self):
        return self._strand.replace('T', 'U')
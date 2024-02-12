from collections import Counter

class DNA:
    def __init__(self, string):
        self._string = string
    
    @property
    def string(self):
        return self._string
    
    def count_nt(self):
        occ = Counter(self._string)
        return [occ[nt] for nt in 'ACGT']
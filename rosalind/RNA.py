from . import DNA

class RNA:
    def __init__(self, strand:DNA):
        self._strand = strand.to_RNA()
        
    @property
    def strand(self):
        return self._strand
from typing import Dict

class Gene:
    @classmethod
    def FASTA(cls, doc:str, type):
        labelled_strings = [string.split('\n') for string in doc.split('>')][1:]
        strings = {repr[0]: type("".join(repr[1:])) for repr in labelled_strings}
        return strings
        
        
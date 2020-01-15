import hashlib
from ..log import logger

s2l = lambda s: [ord(c) for c in s]
l2s = lambda l: ''.join([chr(e) for e in l])

class Str(str):
    def __init__(self, x):
        if isinstance(x, list):
            self.l = x
            self.s = l2s(x)
        elif isinstance(x, str):
            self.s = x
            self.l = s2l(x)
        elif isinstance(x, Str):
            self.s = x.s
            self.l = x.l
        elif isinstance(x, int):
            self.s = str(x)
            self.l = s2l(self.s)
        else:
            raise "Str().__init__() can be initialized with list, str, Str or int."
    
    def __str__(self):
        return self.s
    
    def __add__(self, other):
        return Str(self.s + other.s)
    
    def __radd__(self, other):
        return Str(other.s + self.s)
    
    def __mul__(self, other):
        if isinstance(other,int):
            raise "Str().__mul__() require int"

        return Str(self.s * other)

    def __xor__(self, other, cyclic=False):
        if len(self) != len(other):
            logger.warning("Str().__xor__(): Length is not same.")
        
        return Str([ord(e1)^ord(e2) for (e1,e2) in zip(self, other)])

    def __repr__(self):
        return "'"+self.s+"'"
    
    def __len__(self):
        return len(self.s)
    
    def __getitem__(self,idx):
        return Str(self.s[idx])

    def hex(self, delim=''):
        return Str(delim.join([hex(e)[2:].rjust(2,'0') for e in self.l]))
    
    def hash(self, algo='md5', raw=False):
        hasher = getattr(hashlib, algo)

        if raw:
            return hasher(self.encode())
        else:
            return hasher(self.encode()).hexdigest()

    def xor(self, xoree):
        if not isinstance(xoree, Str) and not isinstance(xoree,str):
            raise "xoree must be Str or str."

        str2 = Str(xoree)
        str2 = str2.pad(xoree, len(self))

        return self^str2

    def pad(self, padee, to_length):
        if not isinstance(padee,Str) and not isinstance(padee, str):
            raise "Str().pad(ee, to_length) : ee must be Str or str."

        return Str(padee * int(to_length/len(padee)) + padee[:to_length%len(padee)])
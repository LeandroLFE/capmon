#!/usr/bin/env python3

from unicodedata import normalize

def remover_acentos(txt):
    if isinstance(txt, str):
        return normalize('NFKD', str(txt)).encode('ASCII', 'ignore').decode('ASCII').strip().lower()
    else:
        ret = []
        for t in txt:
            ret.append(normalize('NFKD', str(t)).encode('ASCII', 'ignore').decode('ASCII').strip().lower())
        return ret
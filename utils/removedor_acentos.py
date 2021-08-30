#!/usr/bin/env python3

from unicodedata import normalize

def remover_acentos(txt):
    return normalize('NFKD', str(txt)).encode('ASCII', 'ignore').decode('ASCII').strip()


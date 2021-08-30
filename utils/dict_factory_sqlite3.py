'''
https://docs.python.org/3/library/sqlite3.html
'''

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
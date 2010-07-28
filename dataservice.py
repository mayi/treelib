# -*- coding: utf-8 -*-

import sqlite3

class DataService():
    def __init__(self):
        self.conn = sqlite3.connect('plant.db')
        self.conn.row_factory = sqlite3.Row

    def queryDataByName(self, name):
        queryStr = '%' + name.strip() + '%';
        c = self.conn.cursor()
        c.execute('select * from plants where name like ?', (queryStr,))
        results = []
        for row in c:
            results.append(row)
        c.close()
        return results

    def queryDataByLatin(self, latin):
        queryStr = '%' + latin.strip() + '%';
        c = self.conn.cursor()
        c.execute('select * from plants where latin like ?', (queryStr,))
        results = []
        for row in c:
            results.append(row)
        c.close()
        return results

    def queryDataByNamesExactly(self, names):
        c = self.conn.cursor()
        results = []
        for name in names:
            if name != '':
                c.execute('select * from plants where name=?',  (name.strip(),))
                if c.rowcount == 0:
                    obj = newEmptyRecord()
                    obj['name'] = name
                    results.append(obj)
                else:
                    for row in c:
                        results.append(row)
        c.close()
        return results
    
    def queryDataByLatinsExactly(self, latins):
        c = self.conn.cursor()
        results = []
        for latin in latins:
            if latin != '':
                c.execute('select * from plants where latin=?',  (latin.strip(),))
                if c.rowcount == 0:
                    obj = newEmptyRecord()
                    obj['latin'] = latin
                    results.append(obj)
                else:
                    for row in c:
                        results.append(row)
        c.close()
        return results

def newEmptyRecord():
    obj = {'name':'', 'latin':'', 'cate':'', 'shxx':'', 'size_qm':'', 'size_gf':'', 'size_gm': '',
           'size_cm':'', 'size_tb':'', 'szsd':'', 'sx':'', 'gstz':'', 'hs':'', 'khlx':'', 'hq':'',
           'fxbw':'', 'gq':'', 'gs':'', 'ys':'', 'zgys':'', 'zttz':'', 'gyz':'', 'nhx':'', 'sfyz':'',
           'tryz':'', 'kx':'', 'ylyt':'', 'jjyt':'', 'bz':'', 'zrfbq':''}
    return obj

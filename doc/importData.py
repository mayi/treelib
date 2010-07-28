# -*- coding: utf-8 -*-

import pymongo

def importData():
    connect = pymongo.Connection('127.0.0.1')
    db = connect['plantsdb']
    pTable = db.plants
    pTable.remove()
    f = open("data.txt")
    try:
        for line in f:
            step = line.split('#')
            obj = {}
            obj['name'] = step[0]
            obj['latin'] = step[1]
            obj['cate'] = step[2]
            obj['shxx'] = step[3]
            obj['size_qm'] = step[4]
            obj['size_gf'] = step[5]
            obj['size_gm'] = step[6]
            obj['size_cm'] = step[7]
            obj['size_tb'] = step[8]
            obj['szsd'] = step[9]
            obj['sx'] = step[10]
            obj['gstz'] = step[11]
            obj['hs'] = step[12]
            obj['khlx'] = step[13]
            obj['hq'] = step[14]
            obj['fxbw'] = step[15]
            obj['gq'] = step[16]
            obj['gs'] = step[17]
            obj['ys'] = step[18]
            obj['zgys'] = step[19]
            obj['zttz'] = step[20]
            obj['gyz'] = step[21]
            obj['nhx'] = step[22]
            obj['sfyz'] = step[23]
            obj['tryz'] = step[24]
            obj['kx'] = step[25]
            obj['ylyt'] = step[26]
            obj['jjyt'] = step[27]
            obj['bz'] = step[28]
            obj['zrfbq'] = step[29]
            pTable.save(obj)
    finally:
        f.close()



   
if __name__ == '__main__':
    importData()

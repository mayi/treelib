# -*- coding: utf-8 -*-

import sqlite3

def importData():
    conn = sqlite3.connect('../plant.db')
    c = conn.cursor()
    # Create table
    c.execute('''create table plants(name text, latin text, cate text, shxx text, size_qm text, size_gf text, size_gm text,
size_cm text, size_tb text, szsd text, sx text, gstz text, hs text, khlx text, hq text, fxbw text, gq text,
gs text, ys text, zgys text, zttz text, gyz text, nhx text, sfyz text, tryz text, kx text,
ylyt text, jjyt text, bz text, zrfbq text)''')

    f = open("data.txt")
    try:
        for line in f:
            step = line.split('#')
            t=(step[0],step[1],step[2],step[3],step[4],step[5],step[6],step[7],step[8],step[9],step[10],step[11],step[12],step[13],step[14],step[15],step[16],step[17],step[18],step[19],step[20],step[21],step[22],step[23],step[24],step[25],step[26],step[27],step[28],step[29])
            c.execute('insert into plants values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', t)
    finally:
        f.close()
    conn.commit()
    c.close()


   
if __name__ == '__main__':
    importData()

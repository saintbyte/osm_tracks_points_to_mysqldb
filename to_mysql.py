#!/usr/bin/env python
# -*- coding: utf-8

import MySQLdb
import string
import sys

def help():
    print sys.argv[0]+" [FILE]\n\n"
    quit()

def fatalerror(s):
    print s+"\n\n"
    quit()

def storeprocess(curline):
     fh1=open(sys.argv[1]+".curline","w")
     fh1.write(str(curline))
     fh1.close()

def main():
    if (len(sys.argv) < 2 ):
	help()
    try:
      fh = open(sys.argv[1],'r')
    except:      
      fatalerror("File "+sys.argv[1]+" cant open")
    cnt = 0
    db = MySQLdb.connect(host="localhost", user="root", passwd="xxxxxxxxx", db="osm_tracks", charset='utf8')
    cursor = db.cursor()
    for line in fh:
        cnt +=1
        if (cnt < 2):
            continue
        line=line.strip()
        (lat,lon,ele)=line.split(",")
        lat = str(float(lat) / 10000000)
        lon = str(float(lon) / 10000000)
	sql = """INSERT DELAYED INTO tracks(location, elevation)
        VALUES ( POINT( %(lat)s, %(lon)s), %(ele)s)
        """%{"lat":lat, "lon":lon, "ele":ele}
        #print sql
        #print "\n\n\n"
        # исполняем SQL-запрос
        cursor.execute(sql)
        # применяем изменения к базе данных
        #db.commit()
        if (cnt % 100000 == 0):
            db.commit() 
            storeprocess(cnt)
    fh.close()      
if __name__=="__main__":
   main()
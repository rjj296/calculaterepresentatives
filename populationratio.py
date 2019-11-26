#!/usr/bin/env python

import csv
import operator

reps = 0

with open('populationratiodata.csv') as datafile:
    reader = csv.reader(datafile)
    header = next(reader)
    table = [[row[0], int(row[1]), int(row[2]), int(row[3])] for row in reader]
    sortedtable = sorted(table, key=lambda row: row[3], reverse=True)
    for row in sortedtable:
        reps += row[2]
    while reps < 435:
        sortedtable[0][2] += 1
        sortedtable[0][3] = sortedtable[0][1]/sortedtable[0][2]
        sortedtable = sorted(sortedtable, key=lambda row: row[3], reverse=True)
        reps += 1
    sortedtable = sorted(sortedtable, key=lambda row: row[2], reverse=True)
with open('populationratioresults.csv','w') as datafile:
    fieldnames = ["States","Population","Representitives","Ratio"]
    writer = csv.DictWriter(datafile, fieldnames=fieldnames)
    writer.writeheader()
    for row in sortedtable:
        writer.writerow({'States':row[0],'Population':row[1],'Representitives':row[2],'Ratio':row[3]})
#!/usr/bin/env python3
#This update is for getting monthly counts for the whole AY.
import csv
import datetime
import collections
import sys

class OrderedCounter(collections.Counter, collections.OrderedDict):
      pass

if len(sys.argv) != 2:
  print('Please include source filename')
  sys.exit(1)
else:
  filename = sys.argv[1]

with open(sys.argv[1], 'r') as fh, open('gfoutputfile1.csv', 'w') as gfoutputfile1:
  wr1 = csv.writer(gfoutputfile1, dialect='excel')
  reader = csv.DictReader(fh)
  gflist = []
  classlist = []
  majors = []

  for row in reader:
    #print (row['Created at'])
    try:
      dt = datetime.datetime.strptime(row['Created at'],'%m/%d/%Y %I:%M %p')
    except ValueError as e:
      dt = datetime.datetime.strptime(row['Created at'],'%m/%d/%y %H:%M')
    #print (dt)
    dh = dt.strftime('%m/%Y')
    gflist.append(dh)  
    classlist.append(row['Classification'])
    majors.append(row['Majors'])

   #print(gflist)
  count = OrderedCounter(gflist)
  classcount = OrderedCounter(classlist)
  majorscount = OrderedCounter(majors)


  for key, value in count.items():
    wr1.writerow([key,value])
  wr1.writerow([])
  for key, value in classcount.items():
    wr1.writerow([key, value])
  wr1.writerow([])
  for key, value in sorted(majorscount.items(), key=lambda x:-x[1]):
    wr1.writerow([key, value])
  #print (count)
  #print (classcount)
  #print (majorscount)
  
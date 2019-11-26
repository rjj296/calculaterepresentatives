#!/usr/bin/env python

import csv
import operator
import math

# Total number of assignable representatives
seats = 435
# initiate representatives allotted
reps = 0
# Open the source data file for reading. Source file is assumed to have 2 columns:
#    States - List of states
#    Population - Population as of the last Census
with open('data.csv') as datafile:
	# Read the file as a csv
    reader = csv.reader(datafile)
    # Pop the header
    header = next(reader)
    # Create the List and Calculate the initial priority
    table = [[row[0], int(row[1]), 1, int(row[1])/math.sqrt(2)] for row in reader]
    # Sort table based off of calculated priority
    sortedtable = sorted(table, key=lambda row: row[3], reverse=True)
    # Sum the number of reps initially allotted (1 each) to each state.
    for row in sortedtable:
        reps += row[2]
    # Assign representatives. The first row in the table will have the state with the highest priority
    while reps < seats:
    	# Add one to the state with the highest priority
        sortedtable[0][2] += 1
        # Calculate the new priority for that state
        sortedtable[0][3] = sortedtable[0][1]/math.sqrt(sortedtable[0][2]*(sortedtable[0][2]+1))
        # Re-Sort the table with the new priority
        sortedtable = sorted(sortedtable, key=lambda row: row[3], reverse=True)
        # Mark that a rep has been assigned.
        reps += 1
    # Now that all the reps are assigned, sort the table by number of representatives for saving
    sortedtable = sorted(sortedtable, key=lambda row: row[2], reverse=True)
# Open the results file for writing
with open('huntingtonhillresults.csv','w') as datafile:
	# Define the field names for the dictionary
    fieldnames = ["States","Population","Representitives"]
    # Create the writing element
    writer = csv.DictWriter(datafile, fieldnames=fieldnames)
    # Write an initial row containing the field (column) names
    writer.writeheader()
    # Write the sorted table to the file
    for row in sortedtable:
        writer.writerow({'States':row[0],'Population':row[1],'Representitives':row[2]})
# Done
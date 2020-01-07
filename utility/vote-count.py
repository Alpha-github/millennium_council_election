import csv
voteData='../data/cache-db.csv'
with open(voteData) as csvR:
    csvReader=csv.reader(csvR)
    for row in csvReader:
        if row==[]: continue    
        
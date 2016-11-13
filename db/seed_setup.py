# Helper file to automate seed data setup such as creating list of unique players
import csv
import os

source = os.path.join(os.path.dirname(os.path.realpath(__file__)), "seed")
table_name = "Player"
table = os.path.join(source, "{}.csv".format(table_name))
export = os.path.join(source, "{}_export.csv".format(table_name))

player_list = set()

with open(table, 'rb') as csvfile:
    tablereader = csv.reader(csvfile, delimiter=',')
    for row in tablereader:
        player_list.add(','.join([row[1], row[2]]))

with open(export, 'wb') as csvfile:
    tablewriter = csv.writer(csvfile, delimiter=',')
    for i, row in enumerate(player_list, start=1):
        name_parts = row.split(',')
        first_name = name_parts[0]
        last_name = name_parts[1]
        tablewriter.writerow([i, first_name, last_name, ''])

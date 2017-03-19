# Helper file to automate seed data setup such as creating list of unique players from player league
import csv
import os

source = os.path.join(os.path.dirname(os.path.realpath(__file__)), "seed")
input_table = os.path.join(source, "PlayerLeague.csv")
export_table = os.path.join(source, "Player_export.csv")

player_list = set()

# with open(table, 'rb') as csvfile:
#     tablereader = csv.reader(csvfile, delimiter=',')
#     for row in tablereader:
#         player_list.add(','.join([row[1], row[2]]))

# with open(export, 'wb') as csvfile:
#     tablewriter = csv.writer(csvfile, delimiter=',')
#     for i, row in enumerate(player_list, start=1):
#         name_parts = row.split(',')
#         first_name = name_parts[0]
#         last_name = name_parts[1]
#         tablewriter.writerow([i, first_name, last_name, ''])


with open(input_table, 'rb') as csvfile:
    tablereader = csv.reader(csvfile, delimiter=',')
    for row in tablereader:
        player_list.add(','.join([row[4], row[5]]))

with open(export_table, 'wb') as csvfile:
    tablewriter = csv.writer(csvfile, delimiter=',')
    for i, row in enumerate(player_list, start=1):
        name_parts = row.split(',')
        first_name = name_parts[0]
        last_name = name_parts[1]
        tablewriter.writerow([i, first_name, last_name, ''])


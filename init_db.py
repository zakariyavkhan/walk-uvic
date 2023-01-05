import fileinput
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

for line in fileinput.input('travel_nodes.csv'):
    #regex
    cur.execute("INSERT INTO travel_nodes (node_name, node_id) VALUES (?, ?)",
                (travel_nodes[0], travel_nodes[1])
                )

connection.commit()
connection.close()
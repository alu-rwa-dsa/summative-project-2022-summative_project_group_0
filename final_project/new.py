# Import dependencies
from cProfile import label
from csv import reader
import pathlib
from matplotlib import pyplot as plt
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
# Read dataset
G = nx.Graph(label=True)
net = Network(width='100vw', height='100vh')
sources = []
targets = []
list_of_tuples = []
careers_list = []
for path in pathlib.Path("csv_files").iterdir():
    if path.is_file():
       with open(path, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        headers = next(csv_reader)
        # Get all rows of csv from csv_reader object as list of tuples
        list_of_tuples = (list(map(tuple, csv_reader)))
        for i in list_of_tuples:
            print(i)
            G.add_edge(i[1], i[2], name=i[3])
            if i[3] not in careers_list:
                careers_list.append(i[3])
print(G.edges(data=True))
 
# print(len(list_of_tuples))
# G.name = "Careers"
# net.from_nx(G)
# # net.show_buttons()
# net.set_options(''' {"nodes": {
#     "font": {
#       "size": 70
#     }
#   },
#   "edges": {
#     "color": {
#       "inherit": true
#     },
#     "smooth": false
#   },
#   "physics": {
#     "repulsion": {
#       "springLength": 500,
#       "springConstant": 1.2,
#       "nodeDistance": 4385
#     },
#     "minVelocity": 0.75,
#     "solver": "repulsion"
#   }
# }''')
# # net.show_buttons()
# net.show('output.html')




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


def csv_to_graph(folder):
    G = nx.Graph(label=True)
    list_of_tuples = []
    careers_list = []
    try:
        for path in pathlib.Path("csv_files").iterdir():
            if path.is_file():
                with open(path, 'r') as read_obj:
                    # pass the file object to reader() to get the reader object
                    csv_reader = reader(read_obj)
                    headers = next(csv_reader)
                    # Get all rows of csv from csv_reader object as list of tuples
                    list_of_tuples = (list(map(tuple, csv_reader)))
                    for i in list_of_tuples:
                        if list_of_tuples.index(i) == 0:
                            G.add_node(i[1], color='green')
                        elif list_of_tuples.index(i) == len(list_of_tuples) - 1:
                            G.nodes[i[1]]['color'] ='red'
                        G.add_edge(i[1], i[2], name=i[3])
                        if i[3] not in careers_list:
                            careers_list.append(i[3])
    except FileNotFoundError:
        G.add_node(1, size=400, color='green')
        raise("Ooops. We seem to have lost our data")

    return G, careers_list


    
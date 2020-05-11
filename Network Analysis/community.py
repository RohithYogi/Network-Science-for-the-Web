import igraph
from igraph import *
import numpy as np
import time


import csv
with open("moreno_highschool/out.moreno_highschool_highschool") as f:
    csvreader = csv.reader(f, delimiter = '\t')
    lines = [tuple(line[0].split()) for line in csvreader][2:]

club = igraph.Graph.TupleList(lines, directed = True,edge_attrs = ['weight'])
club.vs['label'] = club.vs['name']
club.es['color'] = ["green" if i["weight"] == '1' else "blue" for i in club.es]

modularity_value = 10
for i in range(len(list(club.vs))):
    club.ebetw = club.edge_betweenness()
    club.edge_width = [i/10 for i in club.ebetw]
    out = plot(club, layout = club.layout("kk"), edge_width = club.edge_width)
    out.save('iteration'+str(i)+'.png')
    maxbet = np.argmax(np.array(club.ebetw))
    club.membership = club.components(mode = "strong").membership

    new_modularity = club.modularity(club.membership)
    print("modularity in ",i,"th iteration ", new_modularity)

    # if new_modularity - modularity_value <= 0.0000005 and new_modularity!=0:
    #     break
    modularity_value = new_modularity

    club.delete_edges(maxbet)
    time.sleep(1)

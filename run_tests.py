#!/usr/bin/python3

from time import time

from alternative.graph import Graph
from alternative.prim import prim
from alternative.kruskal import kruskal, kruskalSorted
import grafo

instance_files = [
    'costa/galesburg_d.net',
    'costa/galesburg_f.net',
##    'costa/korea1.net',
##    'costa/korea2.net',
    'costa/mexico.net',
    'costa/sawmill.net',
    'costa/strike.net',
    'normalizadas/adjnoun.net',
#    'normalizadas/celegans_metabolic.net',
#    'normalizadas/celegansneural.net',
    'normalizadas/dolphins.net',
#    'normalizadas/email.net',
    'normalizadas/football.net',
    'normalizadas/jazz.net',
    'normalizadas/karate.net',
    'normalizadas/lesmis.net',
    'normalizadas/polbooks.net',
]

output_folder = 'tests/'

## PRIM
#"""
file = open(output_folder + 'prim.csv', 'w')
file.write('n;m;algorithm;instance;time\n')
file.close()
for file in instance_files:
    graph = Graph(file)
    print('prim', file, graph.get_nNodes(), graph.get_nEdges())
    with open(output_folder + 'prim.csv', 'a') as log:
        for i in range(30):
            start = time()
            prim(graph)
            runtime = time() - start
            a = [
                str(graph.get_nNodes()),
                str(graph.get_nEdges()),
                "prim",
                file,
                str(runtime*1000),
            ]
            log.write(';'.join(a) + '\n')
#"""        

## KRUSKAL
"""
file = open(output_folder + 'kruskal.csv', 'w')
file.write('n;m;algorithm;instance;time\n')
file.close()
for file in instance_files:
    grafo.load_graph(file)
    print('kruskal', file)
    with open(output_folder + 'kruskal.csv', 'a') as log:
        for i in range(30):
            start = time()
            grafo.kruskal()
            runtime = time() - start
            a = [
                str(len(grafo.nodes)),
                str(int(len(grafo.edges)/2)),
                "kruskal",
                file,
                str(runtime*1000),
            ]
            log.write(';'.join(a) + '\n')
#"""

## KRUSKAL sorted
"""
file = open(output_folder + 'kruskalSorted.csv', 'w')
file.write('n;m;algorithm;instance;time\n')
file.close()
for file in instance_files:
    graph = Graph(file)
    print('kruskalSorted', file)
    with open(output_folder + 'kruskalSorted.csv', 'a') as log:
        for i in range(30):
            start = time()
            kruskalSorted(graph)
            runtime = time() - start
            a = [
                str(graph.get_nNodes()),
                str(graph.get_nEdges()),
                "kruskalSorted",
                file,
                str(runtime*1000),
            ]
            log.write(';'.join(a) + '\n')
"""



from itertools import product

import networkx as nx
from scipy.spatial import distance

from .abssimcomplex import SimplicialComplex


class VietorisRipsComplex(SimplicialComplex):
    def __init__(
            self,
            points,
            epsilon,
            labels=None,
            distfcn=distance.euclidean
    ):
        super(VietorisRipsComplex, self).__init__()
        self.pts = points
        self.labels = (list(range(len(self.pts)))
                       if labels is None or len(labels) != len(self.pts)
                       else labels)
        self.epsilon = epsilon
        self.distfcn = distfcn
        self.network = self.construct_network(
            self.pts, self.labels, self.epsilon, self.distfcn
        )
        self.import_simplices(map(tuple, nx.find_cliques(self.network)))

    def construct_network(self, points, labels, epsilon, distfcn):
        g = nx.Graph()
        g.add_nodes_from(labels)
        for pair in product(zip(points, labels), zip(points, labels)):
            if pair[0][1] != pair[1][1]:
                dist = distfcn(pair[0][0], pair[1][0])
                if dist < epsilon:
                    g.add_edge(pair[0][1], pair[1][1])
        return g

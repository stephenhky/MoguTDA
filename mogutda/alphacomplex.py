
from scipy.spatial import Delaunay, distance

from .abssimcomplex import SimplicialComplex
from . import facesiter, get_allpoints


def calculate_distmatrix(points, labels, distfcn):
    return {(labels[i], labels[j]): distfcn(points[i], points[j])
            for i in range(len(labels)) for j in range(len(labels))}


def contain_detachededges(simplex, distdict, epsilon):
    if len(simplex) == 2:
        return (distdict[simplex[0], simplex[1]] > 2*epsilon)
    else:
        for face in facesiter(simplex):
            contained = contain_detachededges(face, distdict, epsilon)
            if contained:
                return True
        return False


class AlphaComplex(SimplicialComplex):
    def __init__(self,
                 points,
                 epsilon,
                 labels=None,
                 distfcn=distance.euclidean):
        self.pts = points
        self.labels = (range(len(self.pts))
                       if (labels is None or len(labels) != len(self.pts))
                       else labels)
        self.epsilon = epsilon
        self.distfcn = distfcn
        self.import_simplices(self.construct_simplices(self.pts,
                                                       self.labels,
                                                       self.epsilon,
                                                       self.distfcn))

    def construct_simplices(self, points, labels, epsilon, distfcn):
        distdict = calculate_distmatrix(points, labels, distfcn)

        delaunayobj = Delaunay(points)

        simplices = []
        for simplexnda in delaunayobj.simplices:
            simplex = tuple(simplexnda)

            detached = [contain_detachededges(face, distdict, epsilon) for face in facesiter(simplex)]

            if True in detached and len(simplex) > 2:
                simplices += [face for face, notkeep in zip(facesiter(simplex), detached)
                              if not notkeep]
            else:
                simplices.append(simplex)
        simplices = map(lambda simplex: tuple(sorted(simplex)), simplices)
        simplices = list(set(simplices))

        allpts = get_allpoints(simplices)
        simplices += [(point,) for point in (set(labels)-allpts)]

        return simplices

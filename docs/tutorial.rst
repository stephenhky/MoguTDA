Tutorial
========

To establish a simplicial complex for a torus, type

>>> import numpy as np
>>> from mogutda import SimplicialComplex
>>> torus_sc = [(1,2,4), (4,2,5), (2,3,5), (3,5,6), (5,6,1), (1,6,2), (6,7,2), (7,3,2),
                (1,3,4), (3,4,6), (4,6,7), (4,5,7), (5,7,1), (7,3,1)]
>>> torus_c = SimplicialComplex(simplices=torus_sc)


To retrieve its Betti numbers, type:

>>> print(torus_c.betti_number(0))   # print 1
>>> print(torus_c.betti_number(1))   # print 2
>>> print(torus_c.betti_number(2))   # print 1

To visually present the topology, type:

>>> torus_c.draw()

Home: :doc:`index`

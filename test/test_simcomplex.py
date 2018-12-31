
import unittest
import numpy as np

from mogutda import SimplicialComplex, AlphaComplex


# Simplicial Complex
# ring
ring1d_sc = [(i, i+1) for i in range(10)] + [(10,0)]
# cylinder with hole
cylinder_sc = [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)]
# torus (https://page.mi.fu-berlin.de/rote/Papers/pdf/Computational+topology:+an+introduction.pdf)
torus_sc = [(1,2,4), (4,2,5), (2,3,5), (3,5,6), (5,6,1), (1,6,2), (6,7,2), (7,3,2),
            (1,3,4), (3,4,6), (4,6,7), (4,5,7), (5,7,1), (7,3,1)]
# sphere
twosphere_c = [(1,3,4), (1,2,3), (2,3,4), (1,2,4)]

# Alpha Complex
# circular ring
ring = np.array([np.random.normal(loc=1, scale=0.01)*np.array([np.cos(t), np.sin(t)]) for t in np.linspace(0, 2*np.pi, 101)])[1:]
# spherical ball
sphere = np.array([[np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)] for theta in np.linspace(0.02, np.pi, 51) for phi in np.linspace(0.02, 2*np.pi, 51)])


class test_simcomplex(unittest.TestCase):
    def setUp(self):
        self.sc1 = SimplicialComplex(simplices=[(1, 2), (2, 3), (1, 2, 3)])
        self.sc2 = AlphaComplex(ring, 0.05)
        self.ring1d = SimplicialComplex(simplices=ring1d_sc)
        self.cylinder = SimplicialComplex(simplices=cylinder_sc)
        self.torus = SimplicialComplex(simplices=torus_sc)
        self.twosphere = SimplicialComplex(simplices=twosphere_c)

    def tearDown(self):
        pass

    def test_ring1d(self):
        self.assertEqual(self.ring1d.betti_number(0), 1)
        self.assertEqual(self.ring1d.betti_number(1), 1)
        self.assertEqual(self.ring1d.betti_number(2), 0)

    def test_cylinder(self):
        self.assertEqual(self.cylinder.betti_number(0), 1)
        self.assertEqual(self.cylinder.betti_number(1), 0)
        self.assertEqual(self.cylinder.betti_number(2), 1)
        self.assertEqual(self.cylinder.euler_characteristics(), 2)

    def test_torus(self):
        self.assertEqual(self.torus.betti_number(0), 1)
        self.assertEqual(self.torus.betti_number(1), 2)
        self.assertEqual(self.torus.betti_number(2), 1)
        self.assertEqual(self.torus.betti_number(3), 0)
        self.assertEqual(self.torus.euler_characteristics(), 0)

    def test_twosphere(self):
        self.assertEqual(self.twosphere.betti_number(0), 1)
        self.assertEqual(self.twosphere.betti_number(1), 0)
        self.assertEqual(self.twosphere.betti_number(2), 1)
        self.assertEqual(self.twosphere.euler_characteristics(), 2)

    def test_sc1(self):
        self.assertEqual(self.sc1.betti_number(0), 1)
        self.assertEqual(self.sc1.betti_number(1), 0)
        self.assertEqual(self.sc1.betti_number(2), 0)
        self.assertEqual(self.sc1.euler_characteristics(), 1)

    def test_sc2(self):
        self.assertEqual(self.sc2.betti_number(0), 1)
        self.assertEqual(self.sc2.betti_number(1), 1)
        self.assertEqual(self.sc2.betti_number(2), 0)
        self.assertEqual(self.sc2.euler_characteristics(), 0)

    # def test_sc2_sparse(self):
    #     self.assertEqual(self.sc2.betti_number(0, eps=0.001), 1)
    #     self.assertEqual(self.sc2.betti_number(1, eps=0.001), 1)
    #     self.assertEqual(self.sc2.betti_number(2, eps=0.001), 0)



if __name__ == '__main__':
    unittest.main()
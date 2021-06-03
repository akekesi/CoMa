# CoMaII - PA_07_unittest - Triangulierung
# Attila Kekesi

import unittest
from CoMa_II_PA_07 import *

class Test(unittest.TestCase):
    def test_00(self):
	    # Test von HA07
        n = 4
        triangles = [[0,1,2],[0,2,3]]
        T = ngonTriang(n,triangles)
        print(f'Triangles:\t{T.triangles}')
        print(f'Walls:\t\t{T.walls}')
        self.assertEqual(T.triangles,triangles)
        self.assertEqual(T.walls,[[0,2]])
        self.assertEqual(T.n_walls(),1)
        S = T.flip([0,2])
        self.assertEqual(S.triangles,[[0, 1, 3], [1, 2, 3]])
        self.assertEqual(T.triangles,[[0, 1, 2], [0, 2, 3]])

    def test_01(self):
        # Test von HA07
        n = 4
        triangles = [[0,1,2],[0,2,3],[1,2,3]]
        with self.assertRaises(Exception): ngonTriang(n,triangles)

    def test_02(self):
        n = 3
        triangles = [[0,1,2]]
        T = ngonTriang(n,triangles)
        print(f'Triangles:\t{T.triangles}')
        print(f'Walls:\t\t{T.walls}')
        self.assertEqual(T.triangles,triangles)
        self.assertEqual(T.walls,[])
        self.assertEqual(T.n_walls(),0)

    def test_03(self):
        n = 5
        triangles = [[0,1,2],[0,2,3],[0,3,4]]
        T = ngonTriang(n,triangles)
        print(f'Triangles:\t{T.triangles}')
        print(f'Walls:\t\t{T.walls}')
        self.assertEqual(T.triangles,triangles)
        self.assertEqual(T.walls,[[0,2],[0,3]])
        self.assertEqual(T.n_walls(),2)
        S = T.flip([0,2])
        self.assertEqual(S.triangles,[[0,1,3],[1,2,3],[0,3,4]])
        self.assertEqual(T.triangles,[[0,1,2],[0,2,3],[0,3,4]])

    def test_04(self):
        n = 5
        triangles = [[0,1,2],[0,2,4],[2,3,4]]
        T = ngonTriang(n,triangles)
        print(f'Triangles:\t{T.triangles}')
        print(f'Walls:\t\t{T.walls}')
        self.assertEqual(T.triangles,triangles)
        self.assertEqual(T.walls,[[0,2],[2,4]])
        self.assertEqual(T.n_walls(),2)
        S = T.flip([0,2])
        self.assertEqual(S.triangles,[[0,1,4],[1,2,4],[2,3,4]])
        self.assertEqual(T.triangles,[[0,1,2],[0,2,4],[2,3,4]])

    def test_05(self):
        n = 6
        triangles = [[0,1,2],[0,2,3],[0,3,4],[0,4,5]]
        T = ngonTriang(n,triangles)
        print(f'Triangles:\t{T.triangles}')
        print(f'Walls:\t\t{T.walls}')
        self.assertEqual(T.triangles,triangles)
        self.assertEqual(T.walls,[[0,2],[0,3],[0,4]])
        self.assertEqual(T.n_walls(),3)
        # flip

    def test_06(self):
        n = 6
        triangles = [[0,1,2],[0,2,4],[0,4,5],[2,3,4]]
        T = ngonTriang(n,triangles)
        print(f'Triangles:\t{T.triangles}')
        print(f'Walls:\t\t{T.walls}')
        self.assertEqual(T.triangles,triangles)
        self.assertEqual(T.walls,[[0,2],[2,4],[0,4]])
        self.assertEqual(T.n_walls(),3)
        # flip

    def test_07(self):
        n = 6
        triangles = [[0,1,2],[0,2,3],[0,4,5],[2,3,4]]
        with self.assertRaises(Exception): ngonTriang(n,triangles)

if __name__ == "__main__":
    unittest.main()
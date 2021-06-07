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
        self.assertEqual(S.walls,[[1,3]])
        self.assertEqual(T.triangles,triangles)

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
        S = T.flip([])
        self.assertEqual(S.triangles,triangles)
        self.assertEqual(S.walls,[])
        self.assertEqual(T.triangles,triangles)


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
        self.assertEqual(S.triangles,[[0,1,3],[0,3,4],[1,2,3]])
        self.assertEqual(S.walls,[[0,3],[1,3]])
        self.assertEqual(T.triangles,triangles)

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
        self.assertEqual(S.walls,[[1,4],[2,4]])
        self.assertEqual(T.triangles,triangles)

    def test_05(self):
        n = 6
        triangles = [[0,1,2],[0,2,3],[0,3,4],[0,4,5]]
        T = ngonTriang(n,triangles)
        print(f'Triangles:\t{T.triangles}')
        print(f'Walls:\t\t{T.walls}')
        self.assertEqual(T.triangles,triangles)
        self.assertEqual(T.walls,[[0,2],[0,3],[0,4]])
        self.assertEqual(T.n_walls(),3)
        S = T.flip([0,3])
        self.assertEqual(S.triangles,[[0,1,2],[0,2,4],[0,4,5],[2,3,4]])
        self.assertEqual(S.walls,[[0,2],[0,4],[2,4]])
        self.assertEqual(T.triangles,triangles)

    def test_06(self):
        n = 6
        triangles = [[0,1,2],[0,2,4],[0,4,5],[2,3,4]]
        T = ngonTriang(n,triangles)
        print(f'Triangles:\t{T.triangles}')
        print(f'Walls:\t\t{T.walls}')
        self.assertEqual(T.triangles,triangles)
        self.assertEqual(T.walls,[[0,2],[0,4],[2,4]])
        self.assertEqual(T.n_walls(),3)
        S = T.flip([2,4])
        self.assertEqual(S.triangles,[[0,1,2],[0,2,3],[0,3,4],[0,4,5]])
        self.assertEqual(S.walls,[[0,2],[0,3],[0,4]])
        self.assertEqual(T.triangles,triangles)

    def test_07(self):
        n = 6
        triangles = [[0,1,2],[0,2,3],[0,4,5],[2,3,4]]
        with self.assertRaises(Exception): ngonTriang(n,triangles)

    def test_08(self):
        n = 8
        triangles = [[0,1,7],[1,3,7],[1,2,3],[3,6,7],[3,4,5],[3,5,6]]
        T = ngonTriang(n,triangles)
        print(f'Triangles:\t{T.triangles}')
        print(f'Walls:\t\t{T.walls}')
        self.assertEqual(T.triangles,sorted(triangles))     # triangles war nicht sorted
        self.assertEqual(T.walls,[[1,3],[1,7],[3,5],[3,6],[3,7]])
        self.assertEqual(T.n_walls(),5)
        S = T.flip([3,6])
        self.assertEqual(S.triangles,[[0,1,7],[1,2,3],[1,3,7],[3,4,5],[3,5,7],[5,6,7]])
        self.assertEqual(S.walls,[[1,3],[1,7],[3,5],[3,7],[5,7]])
        self.assertEqual(T.triangles,sorted(triangles))     # triangles war nicht sorted

if __name__ == "__main__":
    unittest.main()
from PA_02 import *
import unittest

class Test(unittest.TestCase):
    def test_output(self):
        self.assertEqual(
            get_lattice_point_number(5, -2, 5, 0, 9),
            "Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt 1."
        )
        self.assertEqual(
            get_lattice_point_number(5, -2, 4, 1, 9),
            "Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt 4."
        )
        self.assertEqual(
            get_lattice_point_number(5, -2, -2, -1, -1),
            "Der Schnitt der gegebenen Rechtecke ist leer."
        )
        self.assertEqual(
            get_lattice_point_number(5, 0, 0, 2, 2),
            "Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt 9."
        )
        self.assertEqual(
            get_lattice_point_number(5, -1, -1, 2, 2),
            "Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt 9."
        )
        self.assertEqual(
            get_lattice_point_number(5, -1, -1, 3, 2),
            "Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt 12."
        )
        self.assertEqual(
            get_lattice_point_number(5, -1, -1, 8, 8),
            "Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt 42."
        )
        self.assertEqual(
            get_lattice_point_number(5, 2, 2, 4, 4),
            "Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt 9."
        )

    def test_basic(self):
        self.assertEqual(get_delta_x1(0, 0), 0)
        self.assertEqual(get_delta_x1(0, 1), 1)
        self.assertEqual(get_delta_x1(1, 1), 0)
        self.assertEqual(get_delta_x1(2, 3), 1)
        self.assertEqual(get_delta_x1(2, 4), 2)
        self.assertEqual(get_delta_x1(4, 6), 2)
        self.assertEqual(get_delta_x1(4, 8), 2)
        self.assertEqual(get_delta_x1(5, 8), 1)
        self.assertEqual(get_delta_x1(-1, 8), 6)

        self.assertEqual(intersects(6, 0, 0, 1, 1), True)
        self.assertEqual(intersects(6, 0, 1, 1, 1), True)
        self.assertEqual(intersects(6, 1, 1, 1, 1), True)
        self.assertEqual(intersects(6, 1, 1, 2, 3), True)
        self.assertEqual(intersects(6, 1, 1, 2, 4), True)
        self.assertEqual(intersects(6, 1, 1, 4, 6), True)
        self.assertEqual(intersects(6, 1, 1, 4, 8), True)
        self.assertEqual(intersects(6, 1, 1, 5, 8), True)
        self.assertEqual(intersects(6, -1, 1, 1, 8), True)
        self.assertEqual(intersects(2, 2, 4, 3, 5), False)
        self.assertEqual(intersects(2, 2, 4, 3, 5), False)
        self.assertEqual(intersects(2, 2, 3, 2, 4), False)
        self.assertEqual(intersects(0, 0, 0, 0, 0), True)
        self.assertEqual(intersects(6, 1, 1, 2, 2), True)
        self.assertEqual(intersects(6, 0, 0, 0, 0), True)
        self.assertEqual(intersects(6, 0, 0, 1, 1), True)
        self.assertEqual(intersects(6, -2, -2, -1, -1), False)

if __name__ == "__main__":
    unittest.main()
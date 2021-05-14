# CoMaII - PA_03_unittest - Topologische Sortierung
# Attila Kekesi
# https://www.youtube.com/watch?v=I6gjCZl7xFw
# https://www.youtube.com/watch?v=4hAqEjj7IdE

import unittest
from CoMa_II_PA_03 import *

class Test(unittest.TestCase):

	def test_00(self):
		# Test trivial
		m = Node()
		n = Node()
		m.name = "M"
		n.name = "N"
		m.color = n.color = "white"
		m.successors = []
		n.successors = []
		G = []
		self.assertEqual(top_order(G), [])
		G = [m]
		self.assertEqual(top_order(G), ["M"])
		G = [n]
		self.assertEqual(top_order(G), ["N"])
		G = [m,n]
		self.assertEqual(top_order(G), ["M","N"])
		G = [n,m]
		self.assertEqual(top_order(G), ["N","M"])


	def test_01(self):
    	# Test vom Uebungsblatt
		n = Node()
		m = Node()
		n.name = "Quelle"
		m.name = "Senke"
		n.color = m.color = "white"
		n.successors = [m]
		m.successors = []
		G = [m,n]
		self.assertEqual(top_order(G), ['Quelle', 'Senke'])

		n = Node()
		m = Node()
		n.name = "links"
		m.name = "rechts"
		n.color = m.color = "white"
		n.successors = [m]
		m.successors = [n]
		G = [m,n]
		self.assertEqual(top_order(G), [-1])

	def test_02(self):
		# Test von Videos/Net
		a = Node()
		b = Node()
		c = Node()
		d = Node()
		e = Node()
		f = Node()
		g = Node()
		h = Node()
		i = Node()
		j = Node()
		k = Node()
		l = Node()
		m = Node()
		a.name = "0"
		b.name = "1"
		c.name = "2"
		d.name = "3"
		e.name = "4"
		f.name = "5"
		g.name = "6"
		h.name = "7"
		i.name = "8"
		j.name = "9"
		k.name = "10"
		l.name = "11"
		m.name = "12"

		# adj = [[1,3],[0,2],[1,3],[0,2]]
		a.successors = [b,d]
		b.successors = [a,c]
		c.successors = [b,d]
		d.successors = [a,c]
		G = [a,b,c,d]
		self.assertEqual(top_order(G), [-1])

		a.successors = []
		b.successors = [c]
		c.successors = [f,j]
		d.successors = []
		e.successors = [l]
		f.successors = [d,h]
		g.successors = [e]
		h.successors = [d,k]
		i.successors = [e]
		j.successors = [g,i]
		k.successors = []
		l.successors = []
		#adj = [[1],[2],[5,9],[],[11],[3,7],[4],[3,10],[4],[6,8],[],[]]
		G = [b,c,d,e,f,g,h,i,j,k,l]
		self.assertEqual(top_order(G), ["1","2","9","8","6","4","11","5","7","10","3"])
		#adj = [[],[1],[2],[5,9],[],[11],[3,7],[4],[3,10],[4],[6,8],[],[]]
		G = [a,b,c,d,e,f,g,h,i,j,k,l]
		self.assertEqual(top_order(G), ["0","1","2","9","8","6","4","11","5","7","10","3"])
		#adj = [[],[]]
		G = [a,d]
		self.assertEqual(top_order(G), ["0","3"])

		a.successors = [b]
		b.successors = [c]
		c.successors = [d]
		d.successors = []
		e.successors = [d]
		f.successors = [e]
		g.successors = [f]
		#adj = [[1],[2],[3],[],[3],[4],[5]]
		G = [a,b,c,d,e,f,g]
		self.assertEqual(top_order(G), ["0","1","2","3","6","5","4"])

		a.successors = []
		b.successors = [f]
		c.successors = [b]
		d.successors = []
		e.successors = [b,c,i]
		f.successors = [d,g]
		g.successors = []
		h.successors = [c,j]
		i.successors = [c]
		j.successors = [i]
		#adj = [[],[5],[1],[],[1,2,8],[3,6],[],[2,9],[2],[8]]
		G = [b,c,d,e,f,g,h,i,j]
		self.assertEqual(top_order(G), ["4","8","2","1","5","6","3","7","9"])

		a.successors = [b,c,f,g]
		b.successors = []
		c.successors = []
		d.successors = []
		e.successors = [d]
		f.successors = [d,e]
		g.successors = [c,e,h]
		h.successors = [i]
		i.successors = []
		j.successors = [g,k,l,m]
		k.successors = []
		l.successors = []
		m.successors = []
		G = [a,b,c,d,e,f,g,h,i,j,k,l,m]
		self.assertEqual(top_order(G), ["0","6","7","8","5","4","3","2","1","9","12","11","10"])
		b.successors = [a]
		G = [a,b,c,d,e,f,g,h,i,j,k,l,m]
		self.assertEqual(top_order(G), [-1])
		b.successors = []
		m.successors = [j]
		G = [a,b,c,d,e,f,g,h,i,j,k,l,m]
		self.assertEqual(top_order(G), [-1])
		m.successors = []
		j.successors = [j]
		G = [a,b,c,d,e,f,g,h,i,j,k,l,m]
		self.assertEqual(top_order(G), [-1])
		m.successors = [k]
		k.successors = [m]
		j.successors = [g,k,l,m]
		G = [a,b,c,d,e,f,g,h,i,j,k,l,m]
		self.assertEqual(top_order(G), [-1])
		m.successors = []
		k.successors = []
		d.successors = [f]
		G = [a,b,c,d,e,f,g,h,i,j,k,l,m]
		self.assertEqual(top_order(G), [-1])

		a.successors = [b]
		b.successors = [a]
		c.successors = [b]
		G = [a,b,c]
		self.assertEqual(top_order(G), [-1])

		a.successors = [b]
		b.successors = [c]
		c.successors = []
		G = [a,b,c]
		self.assertEqual(top_order(G), ["0","1","2"])

		a.successors = [e]
		b.successors = [c,d,e,f]
		c.successors = [d,e]
		d.successors = []
		e.successors = []
		f.successors = []
		G = [a,b,c,d,e,f]
		self.assertEqual(top_order(G), ["0","4","1","5","2","3"])

		a.successors = [b]
		b.successors = [c]
		c.successors = [d]
		d.successors = [a]
		e.successors = [a]
		f.successors = [b]
		g.successors = [c]
		h.successors = [d]
		G = [a,b,c,d,e,f,g,h]
		self.assertEqual(top_order(G), [-1])
		d.successors = []
		G = [a,b,c,d,e,f,g,h]
		self.assertEqual(top_order(G), ["4","0","1","2","3","5","6","7"])

		a.successors = []
		b.successors = [c,d]
		c.successors = [d]
		d.successors = []
		e.successors = [f]
		f.successors = [i]
		g.successors = []
		h.successors = [g]
		i.successors = []
		G = [a,b,c,d,e,f,g,h,i]
		self.assertEqual(top_order(G), ["0","1","2","3","4","5","8","7","6"])

		a.successors = [b]
		b.successors = [c]
		c.successors = []
		d.successors = [e]
		e.successors = [b,c,h]
		f.successors = [e]
		g.successors = [f]
		h.successors = []
		G = [a,b,c,d,e,f,g,h]
		self.assertEqual(top_order(G), ["0","1","2","3","4","7","6","5"])
		h.successors = [g]
		G = [a,b,c,d,e,f,g,h]
		self.assertEqual(top_order(G), [-1])
		e.successors = [b,c]
		h.successors = []
		G = [a,b,c,d,e,f,g,h]
		self.assertEqual(top_order(G), ["0","1","2","3","4","6","5","7"])
		e.successors = [b,c,h]
		d.successors = [d]
		G = [a,b,c,d,e,f,g,h]
		self.assertEqual(top_order(G), [-1])



if __name__ == "__main__":
    unittest.main()
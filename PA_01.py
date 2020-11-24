# Polynommultiplikation und Polynomaddition
# Descartes' Vorzeichenregel

def roots(a,b,c,d,e,f):
	# Reihenfolge der Koeff. als Funk.:		f = a2*x^2 + a1*x + a0
	# Reihenfolge der Koeff. als Vektor: 	F = [a0, a1, a2]

	F = [c,b,a]		# Koeff. von Funk_1
	G = [f,e,d]		# Koeff. von Funk_2
	L = len(F)

	C = [0]*(L+3)	# Koeff. von Funk_3
	C[-1] = 1

	s = 0			# Vorzeichenwechsel

# Berechnung der Koeff. von Funk_3
	for n in range(L):
		for m in range(L):
			C[n + m] = C[n + m] + F[n]*G[m]

# Berechnung der Anzahl des Vorzeichenwechsels
	for i in range(1,len(C)):
		if C[i-1] >= 0 and C[i] < 0:
			s = s + 1
		elif C[i-1] < 0 and C[i] >= 0:
			s = s + 1

# Return: Gerade/Ugerade
	if s % 2 == 0:
		return('Das Polynom hat eine gerade Anzahl von positiven reellen Wurzeln.')
	else:
		return('Das Polynom hat eine ungerade Anzahl von positiven reellen Wurzeln.')

# Check
#print(roots(1,-2,-1,2,1,2))
#print(roots(0,0,0,0,0,0))
#print(roots(3,2,1,3,2,1))


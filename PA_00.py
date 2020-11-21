# Funktion, welche die Summe aller natuerlichen Zahlen,
# die echt kleiner als 1000 und durch 6 und 15 teilbar sind, bildet.

def funktion():
	summe = 0
	for n in range(1000):
		if n % 6 == 0 and n % 15 == 0:
			summe = summe + n
	return summe

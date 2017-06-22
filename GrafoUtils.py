
from collections import defaultdict    

class Grafo(object):
    # Inicializador
	def __init__(self, vertices):
		self.V = vertices
		self.grafo = defaultdict(lambda:set()) #Diccionario default para almacenar el grafo como tuplas de dos listas
    # Funcion para agregar un elemento al grafo
	def eje(self, u, v):
	    self.grafo[u].add(v)
	    self.grafo[v].add(u)

	def vertices(self):
 		return self.V

	def vecinos(self, u):
	    for v in self.grafo[u]:
	        yield v

    
def generarGrafoConexo(n): # n vertices, 2n aristas
	from random import seed, randint
	seed()
	grafo = Grafo(n)
	for v in xrange(1, n):
		u = randint(0, v-1)
		grafo.eje(u, v)
	for _ in xrange(n+1):
		u, v = randint(0, n-1), randint(0, n-1)
		while u == v or u in grafo.vecinos(v):
			v = randint(0, n-1)
		grafo.eje(u, v)
	return grafo

def generarSubsetSum(n): # devuelve una tupla (gen_n, t) donde gen_n es un generador del conjunto
                         # y t es el valor a aproximar
	from random import seed, randint
	seed()
	t = randint(10**8, 10**9)
	return ((randint(1, t-1) for _ in xrange(n)), t) # me parecio mejor dejar un generador en vez de una lista
                                                     # para no desperdiciar tiempo de procesamiento ni memoria

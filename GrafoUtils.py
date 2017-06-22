from collections import defaultdict 
from random import seed, randint, choice   

class Grafo(object):
	def __init__(self, vertices):
		self.V = range(vertices)
		self.grafo = defaultdict(lambda:defaultdict(int)) # grafo[u][v] = cant de aristas entre u y v
		self.contraidos = defaultdict(list) # contraidos[v] = nodos que absorbio v

	def eje(self, u, v):
	    self.grafo[u][v] += 1
	    self.grafo[v][u] += 1

	def vertices(self):
 		return self.V

	def vecinos(self, u):
	    for v in self.grafo[u]:
	    	if self.grafo[u][v]:
		        yield v

	def contraer(self, u, v):
		for w in self.grafo[v]:
			if self.grafo[v][w] and	w != v and w != u:
				self.grafo[u][w] += 1
				self.grafo[w][u] += 1
			self.grafo[w][v] = 0
		self.grafo[v] = defaultdict(int)
		self.contraidos[u].extend([v] + self.contraidos[v])
		self.V.remove(v)

	def ejeRandom(self):
		return choice([(u, v) for v in self.V for u in self.grafo[v] for _ in xrange(self.grafo[u][v]) if u != v])

	def getContraidos(self, u):
		for v in self.contraidos[u]:
			yield v
    
def generarGrafoConexo(n): # n vertices, 2n aristas
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
	seed()
	t = randint(10**8, 10**9)
	return ((randint(1, t-1) for _ in xrange(n)), t) # me parecio mejor dejar un generador en vez de una lista
                                                     # para no desperdiciar tiempo de procesamiento ni memoria

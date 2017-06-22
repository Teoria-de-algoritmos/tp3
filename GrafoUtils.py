
from collections import defaultdict    

def parse(clase, ruta_archivo):
    archivo = open(ruta_archivo)
    grafo = clase(int(archivo.readline())) 
    for _ in xrange(int(archivo.readline())):
        grafo.eje(*map(int, archivo.readline().split()))
    return grafo



class Digrafo(object):
    # Inicializador
	def __init__(self, vertices):
		self.V = vertices
		self.grafo = defaultdict(lambda:(set(),set())) #Diccionario default para almacenar el grafo como tuplas de dos listas
    # Funcion para agregar un elemento al grafo
	def eje(self, u, v):
	    self.grafo[u][0].add(v)
	    self.grafo[v][1].add(u)

	def vertices(self):
 		return self.V

	def vecinos(self, u):
	    for v in self.grafo[u][0]:
	        yield v
    
	def vecinos_entrantes(self, u):
	    for v in self.grafo[u][1]:
	        yield v
            
class Grafo(Digrafo):
    def eje(self, u, v):
    	Digrafo.eje(self, u, v)
    	Digrafo.eje(self, v, u)

class DigrafoConPeso(Digrafo):
	def __init__(self, vertices):
		super(DigrafoConPeso, self).__init__(vertices)
		self.pesos = defaultdict(lambda :float("inf"))

	def eje(self, u, v, peso):
		self.pesos[(u, v)] = peso
		super(DigrafoConPeso, self).eje(u,v)

	def peso(self, u, v):
		return self.pesos[(u,v)]
    
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


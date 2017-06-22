from GrafoUtils import Grafo, generarGrafoConexo

g = generarGrafoConexo(10)
while len(g.vertices()) > 2 :
	g.contraer(*g.ejeRandom())

for u in g.vertices():
	print u, [v for v in g.getContraidos(u)]

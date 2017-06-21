def prediction(v):
	buy, sell = 0, 0
	for i in xrange(len(v)):
		if v[i] < v[buy] :
			buy = i
		if v[sell] - v[buy] < (v[i] - v[buy]):
			sell = i
	return (buy, sell)

valores = [1, 5, 4, 0.5, 4.5, 4, 1, 6, 9, 20, 0.1, 20]
n = len(valores)
buy, sell = prediction(valores)
print "Buy time: " + str(buy)
print "Sell time: " + str(sell)
print "Result: " + str(valores[sell] - valores[buy])

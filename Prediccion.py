def prediction(v):
	bestbuy, buy, sell = 0, 0, 0
	for i in xrange(len(v)):
		if v[i] < v[bestbuy] :
			bestbuy = i
		if v[sell] - v[buy] < (v[i] - v[bestbuy]):
			buy, sell = bestbuy, i
	return (buy, sell)

valores = [1, 5, 4, 0.5, 4.5, 4, 1, 6, 9, 20, 0.1, 20]
buy, sell = prediction(valores)
print "Buy time: " + str(buy)
print "Sell time: " + str(sell)
print "Result: " + str(valores[sell] - valores[buy])

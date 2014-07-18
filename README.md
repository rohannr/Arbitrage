Arbitrage
=========

A python tool to find arbitrage opportunities given current exchange rates. Based on the pricenomics.com coding puzzle. http://priceonomics.com/jobs/puzzle/.

<h1>Introduction<h1>

Daily trading volume in currency exchange markets often exceeds $1 trillion. 
Sometimes, these currency pairs drift in a way that creates arbitrage loops where you can convert through a certain sequence of currencies to return a profit in your base currency. This is referred to as an arbitrage loop. For example, you could do the following trades with $100 US and the exchange data below:
			TO 		
		USD 	EUR 	JPY 	BTC
	USD 	- 	0.7779 	102.4590 	0.0083
FROM 	EUR 	1.2851 	- 	131.7110 	0.01125
	JPY 	0.0098 	0.0075 	- 	0.0000811
	BTC 	115.65 	88.8499 	12325.44 	

    Trade $100 to €77.79
    Trade €77.79 to .8751375 BTC
    Trade .8751375 BTC for $101.20965.


<h2>Assumptions</h2>
<ul>
	<li>Market where prices are independent of supply and demand</li>
	<li>Trading/Transaction costs are waived</li>
</ul>

<h1>Data Source</h1>

The currency exchange rates are pulled from http://fx.priceonomics.com/v1/rates/

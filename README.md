Arbitrage
=========

A python tool to find arbitrage opportunities given current exchange rates. 

<h1>Introduction<h1>

Daily trading volume in currency exchange markets often exceeds $1 trillion. With the advent of new crypto-currencies, your knowledge of algorithms, and a good pair of sound-canceling headphones, you're convinced that there could be some profitable arbitrage opportunities to exploit.

Sometimes, these currency pairs drift in a way that creates arbitrage loops where you can convert through a certain sequence of currencies to return a profit in your base currency. This is referred to as an arbitrage loop. For example, you could do the following trades with $100 US and the exchange data below:
			TO 		
		USD 	EUR 	JPY 	BTC
	USD 	- 	0.7779 	102.4590 	0.0083
FROM 	EUR 	1.2851 	- 	131.7110 	0.01125
	JPY 	0.0098 	0.0075 	- 	0.0000811
	BTC 	115.65 	88.8499 	12325.44 	-

    Trade $100 to €77.79
    Trade €77.79 to .8751375 BTC
    Trade .8751375 BTC for $101.20965.


In this puzzle you'll be working in a market where prices are independent of supply and demand. Also, the currency exchange broker is a close friend of ours, so all trading costs are waived.

Your job is to write a program that efficiently finds the best arbitrage opportunities.

Data Source

To access real-time exchange rates, use our API:

http://fx.priceonomics.com/v1/rates/

Output will look like the JSON below, where USD_JPY is the quantity of JPY that you can purchase for 1 USD.

{
USD_JPY: "95.7422091",
USD_USD: "1.0000000",
JPY_EUR: "0.0080872",
BTC_USD: "105.5641218",
...
}

These are not real actual market prices; we've set them algorithmically. They change every second and contain both a periodic and noise component to them. You only have to pull the data once per run of your algorithm.
Task

Given these exchange rates and the promise of riches, write a program (in any language of your choice) that discovers arbitrage opportunities. You can use any technique you'd like, but we like solutions that would scale with larger sets of currencies.

Submitting

Email your program, as well as a sample run where it makes a profit, to brendan@priceonomics.com.

In addition, please share a little about your background and interests, the position you're interested in, and what excites you about Priceonomics in your message.

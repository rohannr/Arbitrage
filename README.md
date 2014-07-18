Arbitrage
=========

A python tool to find arbitrage opportunities given current exchange rates. Based on the pricenomics.com coding puzzle. http://priceonomics.com/jobs/puzzle/.

<h2>Introduction</h2>

Daily trading volume in currency exchange markets often exceeds $1 trillion. 
Sometimes, these currency pairs drift in a way that creates arbitrage loops where you can convert through a certain sequence of currencies to return a profit in your base currency. This is referred to as an arbitrage loop. For example, you could do the following trades with $100 US and the exchange data below:

<table id="rates">
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>TO</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><b>USD</b></td>
    <td><b>EUR</b></td>
    <td><b>JPY</b></td>
    <td><b>BTC</b></td>
  </tr>
  <tr>
    <td></td>
    <td><b>USD</b></td>
    <td>-</td>
    <td>0.7779</td>
    <td>102.4590</td>
    <td>0.0083</td>
  </tr>
   <tr>
    <td>FROM</td>
    <td><b>EUR</b></td>
    <td>1.2851</td>
    <td>-</td>
    <td>131.7110</td>
    <td>0.01125</td>
  </tr>
   <tr>
    <td></td>
    <td><b>JPY</b></td>
    <td>0.0098</td>
    <td>0.0075</td>
    <td>-</td>
    <td>0.0000811</td>
  </tr>
   <tr>
    <td></td>
    <td><b>BTC</b></td>
    <td>115.65</td>
    <td>88.8499</td>
    <td>12325.44</td>
    <td>-</td>
  </tr>
</table>

<ul>
<li>Trade $100 to &euro;77.79</li>
<li>Trade &euro;77.79 to .8751375 BTC</li>
<li>Trade .8751375 BTC for $101.20965.</li>
</ul>
	
<h2>Assumptions</h2>
<ul>
	<li>Market where prices are independent of supply and demand</li>
	<li>Trading/Transaction costs are waived</li>
</ul>


<h2>Approach</h2>

In the graph of currency transactions we need to find a negative cycle. 

 => w1*w2*w3.....*wn > 1
 => log (w1 * w2 * w3 ... ) > log(1)
 => log(w1) + log(w2) + .... log(wn) > 0
 
 => log(w<sub>1</sub>) + log(w<sub>2</sub>) + log(w<sub>3</sub>) ... &lt; 0(taking negative logarithms)
 

We can identify a negative cycle in a graph using the Bellman-Ford algorithm and the predecessor array to obtain the chain of transactions involved in the arbitrage loop
 

<h2>Data Source</h2>

The currency exchange rates are pulled from http://fx.priceonomics.com/v1/rates/

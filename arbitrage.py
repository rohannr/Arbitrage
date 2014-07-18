import math
edges =   {"USD_JPY": "88.3656587", "USD_USD": "1.0000000", "JPY_EUR": "0.0086312", "BTC_USD": "123.7747778", "JPY_BTC": "0.0000922", "USD_EUR": "0.6708991", "EUR_USD": "1.2491360", "EUR_JPY": "127.9840248", "JPY_USD": "0.0110954", "BTC_BTC": "1.0000000", "EUR_BTC": "0.0109364", "BTC_JPY": "12670.3554644", "JPY_JPY": "1.0000000", "BTC_EUR": "91.2994188", "EUR_EUR": "1.0000000", "USD_BTC": "0.0071600"}

edge_sets = [set(k.split("_")) for k,v in edges.iteritems()]
vertices = set.union(*edge_sets)


def arbit(src):


    dist = {v:float("inf") for v in vertices}
    pre = {v:None for v in vertices}
    dist[src] = 0
    v = len(vertices)
    e = len(edges)

    for i in xrange(v-1):
        for edge, wt in edges.iteritems():
            wt = -math.log(float(wt))
            u,v = edge.split("_")
            if dist[v] > dist[u] + wt:
                dist[v] = dist[u] + wt
                pre[v] = u


    for edge, wt in edges.iteritems():
        if dist[u] + (-math.log(float(wt))) < dist[v]:
            curr = src
            path = []
            while curr != v:
                path.append(curr)
                curr = pre[curr]
            path.extend([curr,src])
            print '->'.join(path)
            return
                

for v in vertices:
    arbit(v)


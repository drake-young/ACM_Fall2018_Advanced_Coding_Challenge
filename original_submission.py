def getWinner(P, W, L, G, by):
    while len(P)+len(W) > 1:
        P = W + P
        W = list()
        while len(P) > 1:
            if (len(P)+len(W) - 1) in by and len(W) > 0:
                break
            else:
                print('G%d: %s %s' % (G,P[0],P[1]))
                P = P[2:]
            W.append('W'+str(G))
            L.append('L'+str(G))
            G += 1
    return (G, P, W, L)

def main():
    n = int(input())
    by = [ 2**i for i in range( 1 , int( n**0.5 ) ) ]
    P = ['P'+str(i+1) for i in range(n)]
    L = list()
    W = list()
    G = 1
    (G, P, W, L) = getWinner(P, W, L, G, by)
    Winner = W[0]
    P = L
    W = list()
    (G, P, W, L) = getWinner(P, W, L, G, by)
    Loser = W[0]
    print('G%d: %s %s' % (G,Winner,Loser))

if __name__ == "__main__":
    main()
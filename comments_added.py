def getWinner(P, W, L, G, by):
    # the player list and winners list combine to make the list of available players
    # for the current round. As long as there's enough players to compete, a new round can
    # begin. The outer loop repeats every round until there's only one person remaining
    while len(P)+len(W) > 1:
        # The new player raster is a combination of the available players lists
        P = W + P

        # Reset the winner's list
        W = list()

        # While there's still players in the player list, the round continues to the next
        # game in the round
        while len(P) > 1:
            # round ends prematurely if it's a "by week"
            if (len(P)+len(W) - 1) in by and len(W) > 0:
                break

            # If it isn't a "by week", the next two players in the raster compete
            else:
                # Display the current game
                print('G%d: %s %s' % (G,P[0],P[1]))

                # Remove the players that just competed from the raster
                P = P[2:]

            # Add this round's winner and loser to their appropriate list
            W.append('W'+str(G))
            L.append('L'+str(G))

            # Increment game counter for the next game
            G += 1

    # once the bracket is complete, return the game number, player list, winner list, and loser list
    return (G, P, W, L)

def main():
    # Retrieve number of players (no prompt -- fails test)
    n = int(input())

    # compute which weeks result in by week
    by = [ 2**i for i in range( 1 , int( n**0.5 ) ) ]

    # List of players
    P = ['P'+str(i+1) for i in range(n)]

    # List of losers (losers bracket)
    L = list()

    # List of winners (next round)
    W = list()

    # Game number
    G = 1

    # Run the primary bracket
    (G, P, W, L) = getWinner(P, W, L, G, by)

    # W[0] is the winner of the primary bracket
    Winner = W[0]

    # Set up for losers bracket (list of players is losers, winners list cleared
    P = L
    W = list()

    # Run the losers bracket
    (G, P, W, L) = getWinner(P, W, L, G, by)

    # W[0] is the winner of the losers bracket
    Loser = W[0]

    # One final game is played between the winners of the two brackets
    print('G%d: %s %s' % (G,Winner,Loser))
    return



if __name__ == "__main__":
    main()
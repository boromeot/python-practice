#July 26 2020 9:00pm
#Two player rock paper scissors

#TODO Make rps_result not case sensitive
#Make nice looking output
#Add error checking/handling

def rps_result(p1, p2):
    '''
    Important:
        Player one's input must be p1
        Player two's input must be p2
    Parameters
    ----------
    p1 : String
        Player ones move. Must be Rock, Paper, or Scissors. Is case sensitive.
    p2 : String
        Player twos move. Must be Rock, Paper, or Scissors. Is case sensitive.

    Returns
    -------
    String
        "Player one won.", "Player two won.", "Players tied."
    '''
    #These three variables exist to prevent excessive typing
    p1w = "Player one won."
    p2w = "Player two won."
    pt = "Players tied."
    if p1 == p2:
        return pt
    else:
        if p1 == "rock":
            if p2 == "paper":
                return p2w
            elif p2 == "scissors":
                return p1w
        elif p1 == "paper":
            if p2 == "rock":
                return p1w
            elif p2 == "scissors":
                return p2w
        elif p1 == "scissors":
            if p2 == "rock":
                return p2w
            elif p2 == "paper":
                return p1w

while True:
    p1_move = input("Player one enter your move.")
    p2_move = input("Player two enter your move.")
    print(rps_result(p1_move, p2_move))
    if input("Would you like to play again? y/n") == 'n':
        break
    

        
        
        
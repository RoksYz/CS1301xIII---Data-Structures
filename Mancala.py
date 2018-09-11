def check_winner(List):
    if List[0][1] != 0:
        return "Keep playing!"
    elif List[1][5] != 0:
        return "Keep playing!"
    elif List[0][0] > List[1][6]:
        return "Player 1 wins!"
    elif List[0][0] < List[1][6]:
        return "Player 2 wins!"
    elif List[0][0] == List[1][6]:
        return "Draw!"
    
#print:
#Keep playing!
#Player 1 wins!
#Player 2 wins!
#Draw!
keep_playing = [[5, 2, 0, 2, 6, 8, 1], [1, 6, 8, 0, 4, 1, 4]]
player1_wins = [[27, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 21]]
player2_wins = [[16, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 32]]
game_is_tied = [[24, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 24]]
print(check_winner(keep_playing))
print(check_winner(player1_wins))
print(check_winner(player2_wins))
print(check_winner(game_is_tied))


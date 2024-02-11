import sys

from board import Board
from player import Player, PlayerBuilder, PlayerCreator




class Driver:

    
    def main():
        MAX_PLAYERS = 2
        size = 3
        current_player_index = 0
        player_won = False

        players = []
        playerBuilder = PlayerBuilder()
        playerCreator = PlayerCreator(playerBuilder)
        print("Welcome to Tik-Tok Toe Game!")
        print("Enter the name of the player 1 (X symbol): ")
        name = input()
        players.append(playerCreator.createPlayerWithX(name))
        
        print("Enter the name of the player 2 (O symbol): ")
        name = input()
        players.append(playerCreator.createPlayerWithO(name))
        
        
        board = Board(size)
        
        while True:
            command = input()
            commands = command.split(" ")
            if commands[0] == "exit":
                break
            if player_won or board.no_valid_moves_left():
                continue
            row = int(commands[0]) - 1
            col = int(commands[1]) - 1

            if board.is_move_valid(row, col):
                board.make_move(row, col, players[current_player_index].get_piece())
                if board.has_player_won(row, col, players[current_player_index].get_piece()):
                    player_won = True
                    print(f"{players[current_player_index].get_name()} won the game")
                elif board.no_valid_moves_left():
                    print("Game Over")

                current_player_index += 1
                if current_player_index >= MAX_PLAYERS:
                    current_player_index %= MAX_PLAYERS
            else:
                print("Invalid Move")

if __name__ == "__main__":
    Driver.main()
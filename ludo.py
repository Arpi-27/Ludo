import random

def roll_dice():
    return random.randint(1, 6)

def move_player(position, roll, board_size):
    new_position = position + roll
    if new_position > board_size:
        return position  # Can't move if it exceeds the board size
    return new_position

def play_ludo():
    board_size = 30  # Define the size of the board (e.g., 30 steps)
    player_positions = [0, 0]  # Starting positions for two players
    players = ["Player 1", "Player 2"]
    game_over = False

    print("Welcome to the Ludo game!")
    print(f"First player to reach position {board_size} wins!\n")

    while not game_over:
        for i in range(2):
            input(f"{players[i]}'s turn! Press Enter to roll the dice.")
            roll = roll_dice()
            print(f"{players[i]} rolled a {roll}.")

            new_position = move_player(player_positions[i], roll, board_size)
            player_positions[i] = new_position
            print(f"{players[i]} is now at position {player_positions[i]}.\n")

            if new_position == board_size:
                print(f"Congratulations! {players[i]} wins!")
                game_over = True
                break

if __name__ == "__main__":
    play_ludo()

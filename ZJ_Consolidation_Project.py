import random

#Create roll dice
def roll_dice():
    """Roll three dice and return the result as a list."""
    dice_list = [random.randint(1, 6) for _ in range(3)]
    return dice_list
# tests
# random.seed(42)
# roll_dice() # gets 6, 1, 1
# roll_dice() # gets 6, 3, 2

#Count the occurance of roll dice being the same
def count_occurrences(dice, value):
    """Count the occurrences of a value in a list."""
    count = sum(1 for x in dice if x == value)
    return count
# test
# dice = [6, 1, 1]
# value = 1 
# occurrences = count_occurrences(dice, value)
# print("The value", value, "appears" ,occurrences, "times in the dice list.")

# Fixed & Unfixed dice rolled
def play_turn(player):
    """
    Play a single turn for a player.

    Args:
        player (str): The name of the player.

    Returns:
        int: The score for the turn.
    """
    dice = roll_dice()
    print(player + " rolls: " + str(dice))

    while True:
        if dice[0] == dice[1] == dice[2]:
            print("Tuple out! You rolled three of a kind.")
            return 0

        fixed_dice = []
        unfixed_dice = []
        for die in dice:
            if count_occurrences(dice, die) > 1:
                fixed_dice.append(die)
            else:
                unfixed_dice.append(die)

        if not unfixed_dice:
            print("All dice are fixed: " + str(fixed_dice))
            break

        print("Fixed dice: " + str(fixed_dice) + ", Unfixed dice: " + str(unfixed_dice))
        reroll = input("Do you want to re-roll the unfixed dice? (yes/no): ").strip().lower()

        if reroll != 'yes':
            break

        new_rolls = [random.randint(1, 6) for _ in range(len(unfixed_dice))]
        dice = fixed_dice + new_rolls
        print("New roll: " + str(dice))

    score = sum(dice)
    print(player + " stops with a score of " + str(score) + " for this turn.")
    return score
# tests
# player_name = "Alice" 
# turn_score = play_turn(player_name) 
# print(player_name,"scored " , turn_score, "points this turn.")


#Start of game stats

def initialize_game(target_score, number_of_players):
    """
    Initialize the game with the target score.

    Args:
        target_score (int): The score a player needs to reach to win.
    """
    players = []
    for i in range(number_of_players):
        player_name = input(f"Enter name for player {i + 1}: ")
        players.append(player_name)
    scores = {player: 0 for player in players}
    current_player_index = 0
    return target_score, players, scores, current_player_index
# tests
# target_score = 100
# game_state = initialize_game(target_score)
# print("Game State" , game_state)

#Adding players to game
def add_player(players, scores, player_name):
    """Add a player to the game."""
    players.append(player_name)
    scores[player_name] = 0
#tests
# players = [] 
# scores = {}
# add_player(players, scores, 'Alice')
# add_player(players, scores, 'Bob')
# add_player(players, scores, 'Charlie')
# print("Current players:", players)
# print("Current scores:", scores)

#Game play for scores
def play_game(target_score, players, scores, current_player_index):
    """Play the game until a player reaches the target score."""
    num_players = len(players)    
    while True:
        if current_player_index >= num_players or current_player_index < 0:
            print("Error: current_player_index is out of range.")
            current_player_index = 0  # Reset to first player instead of breaking
        player = players[current_player_index]
        print("\n{player}'s turn:")
        turn_score = play_turn(player)
        scores[player] += turn_score
        print({player} , "'s total score:" , {scores[player]})
        if scores[player] >= target_score:
            print("{player} wins the game with a total score of {scores[player]}!")
            break
        current_player_index = (current_player_index + 1) % num_players
# target_score = 20
# players = ["Alice", "Bob", "Charlie"]
# scores = {player: 0 for player in players}
# current_player_index = 3 
# print(target_score, players, scores, current_player_index)

#Game start main 

# Input scores & players
target_score = int(input("Enter the target score to win the game: "))
number_of_players = int(input("Enter the number of players: "))



# Adding players
def add_players(game, number_of_players):
    for i in range(number_of_players):
        player_name = input("Enter name for player {i + 1}: ")
        game.add_player(player_name)

# Initialize game state
target_score, players, scores, current_player_index = initialize_game(target_score, number_of_players)

# Start playing the game
play_game(target_score, players, scores, current_player_index)
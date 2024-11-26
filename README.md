# Consolidation_Project_ZJ
 
# This Python project uses a simple dice game where players take turns rolling three dice. The objective is to accumulate points by rolling the dice and making strategic decisions on whether to keep or re-roll certain dice. The first player to reach a target score wins the game.

# Features
- Roll three dice and display the results.
- Count occurrences of specific values in the rolled dice.
- Allow players to keep or re-roll certain dice based on their strategy.
- Track scores for multiple players until one reaches the target score.

# Functions: 
roll_dice()
- Rolls three dice and returns the results as a list of integers (each between 1 and 6).

count_occurrences(dice, value)
- Counts how many times a specific value appears in a list of dice rolls.

play_turn(player)
- Conducts a single turn for the specified player.

initialize_game(target_score, number_of_players)
- Initializes the game with a target score and collects player names.

add_player(players, scores, player_name)
- Adds a new player to the game.

play_game(target_score, players, scores, current_player_index)
- Controls the flow of the game until one player reaches or exceeds the target score.

# Initial input for game:
- The target score needed to win the game.
- The number of players participating in the game.
- Each player's name.

# Steps of game
- each player must decide if they want to re-roll the unfix dice 
- if player chooses not to re-roll, round continues to next player
- game ends once player achieves target score. 
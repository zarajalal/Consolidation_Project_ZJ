# Consolidation_Project_ZJ
 
This Python project uses a simple dice game where players take turns rolling three dice. The objective is to accumulate points by rolling the dice and making strategic decisions on whether to keep or re-roll certain dice. The first player to reach a target score wins the game.

# Features
- Roll three dice and display the results.
- Count occurrences of specific values in the rolled dice.
- Allow players to keep or re-roll certain dice based on their strategy.
- Track scores for multiple players until one reaches the target score.
- Calculate the time tracking for each turn


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


# How to play:
1. Run the script.
2. Enter the target score to win the game.
3. Specify the number of players.
4. Enter names for each player.
5. Follow the prompts to play each turn:
    1. Roll the dice
    2. Choose to re-roll unfixed dice or keep your current roll
    3. Accumulate points
6. The game ends when a player reaches or exceeds the target score.

# How to run:
- save/download python script
- enter: ZJ_Consolidation_Project.py in terminal

Example play:
Enter the target score to win the game: 20
Enter the number of players: 2
Enter name for player 1: P1
Enter name for player 2: P2
{'P1'} 's turn:
P1 rolls: [6, 3, 5]
Fixed dice: [], Unfixed dice: [6, 3, 5]
Do you want to re-roll the unfixed dice? (yes/no): no
P1 stops with a score of 14 for this turn.
The time taken for this turn: 3.29961895942688 seconds.
P1 's total score: 14
{'P2'} 's turn:
P2 rolls: [4, 6, 6]
Fixed dice: [6, 6], Unfixed dice: [4]
Do you want to re-roll the unfixed dice? (yes/no): yes
New roll: [6, 6, 3]
Fixed dice: [6, 6], Unfixed dice: [3]
Do you want to re-roll the unfixed dice? (yes/no): no
P2 stops with a score of 15 for this turn.
The time taken for this turn: 4.541433811187744 seconds.
P2 's total score: 15
{'P1'} 's turn:
P1 rolls: [5, 4, 1]
Fixed dice: [], Unfixed dice: [5, 4, 1]
Do you want to re-roll the unfixed dice? (yes/no): yes
New roll: [2, 4, 1]
Fixed dice: [], Unfixed dice: [2, 4, 1]
Do you want to re-roll the unfixed dice? (yes/no): no
P1 stops with a score of 7 for this turn.
The time taken for this turn: 4.919853210449219 seconds.
P1 's total score: 21
{'P1'} wins the game with a total score of {21} !

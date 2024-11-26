import random


def roll_dice():
    """Roll three dice and return the result as a list."""
    dice_list = [random.randint(1, 6) for _ in range(3)]
    return dice_list
# # tests
# random.seed(42)
roll_dice() # gets 6, 1, 1
# roll_dice() # gets 6, 3, 2

def count_occurrences(dice, value):
    """Count the occurrences of a value in a list."""
    count = sum(1 for x in dice if x == value)
    return count
random.seed(42)
roll_dice()
dice = [6, 1, 1]
value = 2 
count_occurrences([6 , 1 ,1 ] , [2])

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



def TupleOutDiceGame(target_score):
    """
    Initialize the game with the target score.

    Args:
        target_score (int): The score a player needs to reach to win.

    Returns:
        dict: A dictionary containing game state information.
    """
    return {
        'target_score': target_score,
        'players': [],
        'scores': {},
        'current_player_index': 0
    }

def add_player(self, player_name):
        """Add a player to the game."""
        self.players.append(player_name)
        self.scores[player_name] = 0

def play_game(self):
        """Play the game until a player reaches the target score."""
        while max(self.scores.values()) < self.target_score:
            player = self.players[self.current_player_index]
            print("\n" + player + "'s turn:")
            turn_score = play_turn(player)
            self.scores[player] += turn_score
            print(player + "'s total score: " + str(self.scores[player]))
            if self.scores[player] >= self.target_score:
                print(player + " wins the game with a total score of " + str(self.scores[player]) + "!")
                break
            self.current_player_index = (self.current_player_index + 1) % len(self.players)


# Main program



target_score = int(input("Enter the target score to win the game: "))
number_of_players = int(input("Enter the number of players: "))

game = TupleOutDiceGame(target_score)

    # Adding players
for i in range(number_of_players):
    player_name = input("Enter name for player " + str(i + 1) + ": ")
    add_player(game, player_name)

    # Play the game
    game.play_game()
    
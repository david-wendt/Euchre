# CS238-Euchre-Project
Final project for Stanford AA228/CS238 to make a Euchre-playing RL agent.

# Potential project structure 

Found this: https://github.com/datamllab/rlcard, but ngl i think this game is simple enough that it would be fun and educational to code up the environment ourselves. I am down to do this if nobody else wants to.

## `game.py`
1) Contains a `GameState` class to encode the state of the game (cards played, tricks won by which player, which player's turn it currently is, who won the bidding, etc)

I was initially thinking of also having a `PlayerState` class to encode private info about each player, but in reality the only private info is their hand, right? So maybe just make the player hands an attribute of the `GameState` and don't feed it to the player/agent when giving them info to make their choice?

2) Make a separate class/function, taking the `GameState` and all player agents as arguments, and making one turn at a time? Or just have a `take_turn` method of the `GameState` which takes the single active player agent as an argument?

## `featurize.py`

Contains a `featurize_game_state` function (which maybe calls helper functions to featurize various parts of the game state) as well as a `featurize_hand` to create feature vectors to pass to our RL agents
- maybe length-52 vector (or, you know, length-n where n is the number of cards in the game. 26? 24?) with 1's in the position of the cards in the hand and 0's elsewhere? I am guessing that just indexing all cards with a single number will be too difficult for a simple RL algorithm to learn, but at the same time
- perhaps, for game state cards played, have a single length-n vector with 1's in the positions of all cards that have been played and separately just one integer per team saying how many tricks won? And then possibly later encoding which players played which cards as part of which tricks?

## `agent.py`

Write up our RL agent here. Maybe first try Q-learning (probably shallow with features rather than enumerating all states) and then deep Q-learning? See if any other algs introduced in class are applicable?

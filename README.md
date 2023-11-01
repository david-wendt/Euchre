# CS238-Euchre-Project
Final project for Stanford AA228/CS238 to make a Euchre-playing RL agent.

# Next steps
1. Test the implementation a bit to make sure nothing is wrong with it
2. Think about what information we want to feed to (at least a first generation) AI model
3. Rewrite some parts of the Euchre code to make sure that all the necessary information can be passed to the Player objects in `Player.play_card`.
4. Think about what kind of model we want to use first. How will we featurize the requisite information?
5. Write functions to featurize everything we need to pass to the first generation model.
6. Implement the model
7. Think about what benchmarks to use. Random choice of a valid card? Some simple deterministic strategy? Are two benchmarks enough?
8. Train and evaluate the model against itself and against benchmarks
9. Think about new models or improvements to the model and iterate through steps 2-8
10. (Optional, probably unnecessary to get full credit for the project) Implement real bidding? Figure out how to train a model to do this as well? two separate models I'm assuming?

# Potential project structure 

## `bidding`/`card`/`display`/`euchre`/`euchre_hand`/`global_info`/`player`.py
Implements Euchre. Finished with all but bidding.

## `featurize.py`

Contains a `featurize_game_state` function (which maybe calls helper functions to featurize various parts of the game state) as well as a `featurize_hand` to create feature vectors to pass to our RL agents
- maybe length-52 vector (or, you know, length-n where n is the number of cards in the game. 26? 24?) with 1's in the position of the cards in the hand and 0's elsewhere? I am guessing that just indexing all cards with a single number will be too difficult for a simple RL algorithm to learn, but at the same time
- perhaps, for game state cards played, have a single length-n vector with 1's in the positions of all cards that have been played and separately just one integer per team saying how many tricks won? And then possibly later encoding which players played which cards as part of which tricks?

## `agent.py`

Write up our RL agent here. Maybe first try Q-learning (probably shallow with features rather than enumerating all states) and then deep Q-learning? See if any other algs introduced in class are applicable?

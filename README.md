# CS238-Euchre-Project
Final project for Stanford AA228/CS238 to make a Euchre-playing RL agent.

# Next steps
1. Test the implementation a bit to make sure nothing is wrong with it
2. Think about what information we want to feed to (at least a first generation) AI model
3. Rewrite some parts of the Euchre code to make sure that all the necessary information can be passed to the Agent objects via `player.play_card` in `game/euchre_hand.py`.
4. Think about what kind of model we want to use first. How will we featurize the requisite information?
5. Write functions to featurize everything we need to pass to the first generation model.
6. Implement the model
7. Think about what benchmarks to use. Random choice of a valid card? Some simple deterministic strategy? Are two benchmarks enough?
8. Train and evaluate the model against itself and against benchmarks
9. Think about new models or improvements to the model and iterate through steps 2-8
10. (Optional, probably unnecessary to get full credit for the project) Implement real bidding? Figure out how to train a model to do this as well? two separate models I'm assuming?

# Potential project structure 

## `game` (folder)

Implements Euchre. Finished with all but bidding.

## `agents` (folder)

One file to implement each agent. Manual and random implemented so far, baseline deterministic outlined. Need to implement varous AI/RL models here.

 Maybe try Q-learning (probably shallow with features rather than enumerating all states) and then deep Q-learning? See if any other algs introduced in class are applicable? Perhaps the POMDP version of rollout lookahead or something as a baseline?


## `featurize`

Make a folder called `featurize` and include one or more files to featurize various properties of the game state? See next paragraph for ideas on functions.

Contains a `featurize_game_state` function (which maybe calls helper functions to featurize various parts of the game state) as well as a `featurize_hand` to create feature vectors to pass to our RL agents
- maybe length-24 vector with 1's in the position of the cards in the hand and 0's elsewhere? I am guessing that just indexing all cards with a single number will be too difficult for a simple RL algorithm to learn. Maybe a good compromise is a 1-hot length-4 vector with the suit, plus an additional single element for the rank, for each card? So 5 entries dedicated to each card? Easier to specify the cards in the hand that way, but harder to represent the set of all cards previously played, for which it would be easier to just have a length-24 vector initialized to 0's where 1's get filled in as tricks get played.
- Would need more complicated features if we want to specify which cards were played as part of which tricks or by which players, but I'd guess we don't quite need that, at least in the beginning.

## `evaluate`

Probably need some evaluation functions to run the game many times with various combinations of agents to get statistics on win rates
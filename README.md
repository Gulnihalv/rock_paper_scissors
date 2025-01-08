# Rock Paper Scissors

This is the boilerplate for the Rock Paper Scissors project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

This is a simple implementation of the Rock-Paper-Scissors game using a Markov Model. The AI predicts the next move based on the player's last three moves and adjusts its probabilities dynamically during the game.

## Features
- Tracks the last three moves of the player to predict the next move.
- Uses a Markov Model to calculate the probabilities of the player's next move.
- AI adapts its strategy in real time based on the player's behavior.

## How It Works
1. **Player's History:** The model stores the last three moves of the player as a sequence.
2. **Prediction:** The model calculates the probabilities for each possible next move (rock, paper, scissors) based on the observed sequences.
3. **AI Move:** The AI selects the move most likely to counter the predicted player move.

## Exponential Decay
The model employs an **Exponential Decay** mechanism to give more weight to recent moves while gradually reducing the influence of older moves.
# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import numpy as np

states = {"R": 0, "P": 1, "S": 2}
reverse_states = {0: "R", 1: "P", 2: "S"}
alpha = 0.1
transition_matrix = np.zeros((3, 3, 3, 3))

def player(prev_play, opponent_history=[]):
    global transition_matrix

    if (not opponent_history):
        opponent_history.extend(["R", "P", "S"])

    if prev_play:
        opponent_history.append(prev_play)

        if len(opponent_history) > 3:
            prev3_state = states[opponent_history[-4]]
            prev2_state = states[opponent_history[-3]]
            prev_state = states[opponent_history[-2]]
            current_state = states[opponent_history[-1]]
            transition_matrix[prev3_state][prev2_state][prev_state][current_state] = (
                (1 - alpha) * transition_matrix[prev3_state][prev2_state][prev_state][current_state] + alpha
            )

    if len(opponent_history) > 3:
        prev3_state = states[opponent_history[-3]]
        prev2_state = states[opponent_history[-2]]
        prev_state = states[opponent_history[-1]]
        next_state = np.argmax(transition_matrix[prev3_state][prev2_state][prev_state])
        pred_move = reverse_states[next_state]
    else:
        pred_move = "R"

    ideal_move = {"R": "P", "P": "S", "S": "R"}
    guess = ideal_move[pred_move]

    return guess

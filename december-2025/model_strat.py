from random import randint
import numpy as np
from typing import Tuple

def play_game(p1_threshold: float, p2_threshold: float, num_simulations: int) -> Tuple[float, float]:
    p1_wins, p2_wins = 0, 0

    for _ in range(num_simulations):
        p1_throw = np.random.uniform(0, 1)
        if p1_throw < p1_threshold:
            p1_throw = np.random.uniform(0, 1)

        p2_throw = np.random.uniform(0, 1)
        if p2_throw < p2_threshold:
            p2_throw = np.random.uniform(0, 1)

        if p1_throw > p2_throw:
            p1_wins += 1
        else:
            p2_wins += 1

    return p1_wins / num_simulations, p2_wins / num_simulations

def main():
    # E[value] = P(keep) * E[X | X >= w] + P(discard) * E[Y]
    p1_threshold, p2_threshold = 0.5, 0.58
    p1_win_rate, p2_win_rate = 0, 1
   
    p1_win_rate, p2_win_rate = play_game(p1_threshold=p1_threshold, p2_threshold=p2_threshold, num_simulations=10_000_000)
    print(f"Player1 win rate: {p1_win_rate}, p1-thres: {p1_threshold}")
    print(f"Player2 win rate: {p2_win_rate}, p2-thres: {p2_threshold}")

    
 

if __name__ == "__main__":
    main()

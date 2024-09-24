from typing import Literal


class Running:
    score: [int, int]
    max_score: int

    def __init__(self, max_score = 5):
        self.score = [0, 0]
        self.max_score = max_score


class Ended:
    winner: Literal["player1", "player2"]

    def __init__(self, winner):
        self.winner = winner


class State:
    current: Running | Ended

    def __init__(self, state=Running()):
        self.current = state

from typing import Literal


class Running:
    score: [int, int]

    def __init__(self):
        self.score = [0, 0]


class Ended:
    winner: Literal["player1", "player2"]

    def __init__(self, winner):
        self.winner = winner


class State:
    current: Running | Ended

    def __init__(self, state=Running()):
        self.current = state

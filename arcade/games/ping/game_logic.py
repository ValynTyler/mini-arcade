class Running:
    scores: [int, int]
    max_score: int

    def __init__(self, max_score=5):
        self.scores = [0, 0]
        self.max_score = max_score

    def check_score(self, on_win_detected=lambda w: None):
        i = 0
        for score in self.scores:
            if score >= self.max_score:
                on_win_detected(i)
                break
            i += 1


class Ended:
    winner: int

    def __init__(self, winner):
        self.winner = winner


State = Running | Ended


class Game:
    state: State

    def __init__(self):
        self.state = Running()

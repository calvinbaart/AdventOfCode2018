from collections import deque

class MarbleGame:
    def __init__(self, num_players):
        self.players = [0] * num_players
        self.marbles = None

    def play(self, max_value):
        self.marbles = deque([0])
        self.current_player = -1
        
        for x in range(1, max_value + 1):
            self.current_player = (self.current_player + 1) % len(self.players)

            if x % 23 is 0:
                self.marbles.rotate(7)
                self.players[self.current_player] = self.players[self.current_player] + x
                self.players[self.current_player] = self.players[self.current_player] + self.marbles.pop()
                self.marbles.rotate(-1)
            else:
                self.marbles.rotate(-1)
                self.marbles.append(x)


if __name__ == "__main__":
    game = MarbleGame(471)
    game.play(max_value=72026)

    print(max(game.players))

from .part1 import MarbleGame

game = MarbleGame(471)
game.play(max_value=72026 * 100)

print(max(game.players))

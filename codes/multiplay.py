from tictactoe import TicTacToe

game = TicTacToe()
game.reset()

while True:
    game.render()
    action = int(input("Player%i Action (0-8):" % game.turn))
    done = game.step(action)
    if done:
        game.render()
        break
print("winner", game.winner)
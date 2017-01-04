from player import Player



class TicTacToe:

    def __init__(self, grid, players):
        self.grid = grid
        self.grid_size = len(grid[0])
        self.players = players
        self.turn = 0
        self.playing = False
        self.current_player = None


    def play(self):
        self.current_player = 0
        self.playing = True

        while self.turn < 10:
            self.draw()
            self.turn += 1

            self.play_turn()

            # Test isGagnant(self.current_player)
            self.current_player = 1 if self.current_player == 0 else 0


    def draw(self):
        print('  1 2 3')
        for line in range(self.grid_size):
            print(str(line + 1) + ' ', end='')
            for column in range(self.grid_size):
                if column != 0:
                    print('|', end='')
                print(self.draw_case(self.grid[line][column]), end='')
            print()
            if line != 2:
                print('  ' + '-' * 5)


    def draw_case(self, case):
        if case == 0:
            return ' '
        elif case == 1:
            return self.players[case-1].draw()
        elif case == 2:
            return self.players[case-1].draw()


    def play_turn(self):
        while True:
            try:
                user_input = input('{}, à vous de jouer (ligne - colonne) : '.format(self.players[self.current_player]))
                line, col = map(lambda x: int(x)-1, user_input.split(' - '))

                if not self.can_play(line, col):
                    print('La case ({}, {}) n\'est pas libre ! Veuillez recommencer.'.format(line+1, col+1))
                else:
                    self.grid[line][col] = self.current_player
                    return
            except ValueError:
                print('Saisie non valide, veuillez recommencer')


    def can_play(self, line, col):
        if (line < 0 or line > self.grid_size) or (col < 0 or col > self.grid_size):
            return False
        else:
            return self.grid[line][col] == 0



if __name__ == '__main__':
    game = TicTacToe(
        [[0]*3 for x in range(3)],
        [Player('Joueur 1', 'X'), Player('Joueur 2', 'O')]
    )
    game.play()

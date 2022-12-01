class Gameboard:
    def __init__(self, hits, occupies):

        self.gridboard = hits
        self.occupied_squares = occupies
        self.alphabet = alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    def hit_position(self, position):

        if self.gridboard[position] == 'unhit' and self.occupied_squares[position] == 'occupied':
            self.gridboard[position] = 'Hit'
            print(f"{position} is a hit!")

        elif self.gridboard[position] == 'hit':
            print(f"You have already hit {position}")

        elif self.gridboard[position] == 'unhit' and self.occupied_squares[position] == 'unoccupied':
            self.gridboard[position] = 'Miss'
            print("You have missed!")

    # def occupy_position(self):

    def ship_placement(self, length, position):
        '''This places ship on the board'''
        starting_pos = []
        conditions = "unmet"
        while conditions == "unmet":
            starting_letter = input("LETTER (A - J): ")
            starting_number = input("NUMBER 1 - 10: ")
            starting_pos += [starting_letter]
            starting_pos += [starting_number]
            starting_square = starting_pos[1] + starting_pos[2]
            if starting_square not in self.occupied_squares.keys():
                print("Must be a valid position")
                continue

            if position == "horizontal":
                letter_pos = starting_square[0]
                number_pos = int(starting_square[1])
                build_occ = number_pos + length
                if build_occ > 9 or number_pos == 0:  # make sure it isn't placed off board
                    print("Ship off board... Try again.")
                    continue
                while number_pos < build_occ:
                    self.occupied_squares[letter_pos + str(number_pos)] = "occupied"
                    number_pos = number_pos + 1


            if position == "vertical":
                letter_pos = starting_square[0]
                number_pos = int(starting_square[1])
                num_of_alphabet = self.alphabet.index(letter_pos)  # need alphabet!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                if num_of_alphabet <= 0 or num_of_alphabet + length > 11:  # make sure it isn't placed off board
                    print("Ship off board... Try again.")
                    continue
                while num_of_alphabet < length:
                    build_occupied_space = self.alphabet[num_of_alphabet] + str(number_pos)
                    self.occupied_squares[build_occupied_space] = "occupied"
                    num_of_alphabet = num_of_alphabet + 1

            conditions = "met"


hit_board = {}
occupy_board = {}


def make_grid(grid, value):  # square_value is condition of square on grid(hit/unit)
    number = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for nums in range(1, 11, 1):
        number = number + 1
        for letters in alphabet:
            grid[letters + str(number)] = value  # return values to dcitionary


make_grid(hit_board, "unhit")
make_grid(occupy_board, "unoccupied")
player_board = Gameboard(hit_board, occupy_board)

ships = {"Aircraft Carrier": 5, "Battleship": 4, "Destroyer": 3, "Submarine": 3, "PT Boat": 2}  # size of ships

for keys, values in ships.items():
    orientation = input(f"You are placing your {keys}.  Which orientation would you like (Vertical or Horizontal)?")
    start_square = input("which sqare will be your starting square left to right/top to bottom")
    player_board.ship_placement(values, orientation)

    player_board.hit_position("j1")
    print(player_board.occupied_squares)

    print("()")

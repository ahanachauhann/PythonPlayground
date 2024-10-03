#crossword puzzle
class CrosswordPuzzle:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.puzzle = [[' ' for _ in range(cols)] for _ in range(rows)]

    def add_word(self, word, row, col, direction):
        if direction == 'horizontal':
            for i, letter in enumerate(word):
                if col + i < self.cols:  
                    self.puzzle[row][col + i] = letter
        elif direction == 'vertical':
            for i, letter in enumerate(word):
                if row + i < self.rows:  
                    self.puzzle[row + i][col] = letter

    def display_puzzle(self):
        for row in self.puzzle:
            for letter in row:
                print(letter, end=' ')
            print()
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
puzzle = CrosswordPuzzle(rows, cols)
num_words = int(input("Enter the number of words to add: "))
for i in range(num_words):
    word = input("Enter word: ")
    row = int(input("Enter the starting row: "))
    col = int(input("Enter the starting column: "))
    direction = input("Enter the direction (horizontal/vertical): ")
    puzzle.add_word(word, row, col, direction)

print("Crossword Puzzle:")
puzzle.display_puzzle()

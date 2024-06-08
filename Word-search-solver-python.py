def print_board(board):
    """Prints the word search board."""
    for row in board:
        print(" ".join(row))

def find_word(board, word):
    """Finds the word in the board and returns the starting and ending coordinates."""
    rows = len(board)
    cols = len(board[0])
    
    def search_direction(x, y, dx, dy):
        """Searches in a specific direction."""
        for i in range(len(word)):
            if x + i * dx < 0 or x + i * dx >= rows or y + i * dy < 0 or y + i * dy >= cols:
                return False
            if board[x + i * dx][y + i * dy] != word[i]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            if board[x][y] == word[0]:
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if search_direction(x, y, dx, dy):
                        return (x, y), (x + (len(word) - 1) * dx, y + (len(word) - 1) * dy)
    return None

def solve_word_search(board, words):
    """Solves the word search puzzle and returns the positions of each word."""
    results = {}
    for word in words:
        position = find_word(board, word)
        if position:
            results[word] = position
    return results

# Get user input for the word search board
board = []
print("Enter the letters for each row of the word search board, separated by spaces:")
for i in range(9):  # Assuming a 9x9 board for this example
    row = input(f"Row {i + 1}: ").split()
    board.append(row)

# Get user input for the words to find
words = []
num_words = int(input("How many words do you want to find? "))
for _ in range(num_words):
    word = input("Enter word: ")
    words.append(word)

print("\nWord Search Board:")
print_board(board)
print("\nWords to find:", words)
print("\nSolving...\n")

# Solve the word search
results = solve_word_search(board, words)

for word, pos in results.items():
    start, end = pos
    print(f"Word '{word}' found from {start} to {end}")

if not results:
    print("No words found.")

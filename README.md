# word-search-solver
This Python script allows you to input a word search board and a list of words to find within that board. It then searches for each word in the board and returns the starting and ending coordinates of each word if found.

Functions
print_board(board): Prints the word search board.
find_word(board, word): Finds the word in the board and returns the starting and ending coordinates.
solve_word_search(board, words): Solves the word search puzzle and returns the positions of each word.

How to Use Input Word Search Board:

Run the script and follow the prompts to enter the letters for each row of the word search board. The board should be separated by spaces.
Example:
Enter the letters for each row of the word search board, separated by spaces:
Row 1: A B C D E F G H I
Row 2: J K L M N O P Q R
...


Input Words to Find:

Enter the number of words you want to find.
Enter each word one by one.
Example:
How many words do you want to find? 3
Enter word: APPLE
Enter word: ORANGE
Enter word: BANANA
View Results:


The script will display the word search board and the words to find.
It will then solve the word search puzzle and display the positions of each word found.
Example:


Word Search Board:
A B C D E F G H I
J K L M N O P Q R
...

Words to find: ['APPLE', 'ORANGE', 'BANANA']

Solving...

Word 'APPLE' found from (0, 0) to (0, 4)
Word 'ORANGE' found from (1, 0) to (1, 5)
Word 'BANANA' found from (2, 0) to (2, 5)

No Words Found: If no words are found in the board, it will display "No words found."

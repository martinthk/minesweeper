# minesweeper
A single-player game

## The Game
The game starts with a grid of unmarked squares. 

The game is played by asking the user to either step on one of these squares to reveal its content or flag that square as a mine.

If a square containing a mine is revealed, the player loses the game otherwise a number is displayed in the square, indicating how many adjacent squares contain mines. If no mines are adjacent, then all adjacent squares will be revealed.

The player uses the numbers displayed in the squares to deduce the contents of other squares, and may either safely reveal each square or flag the squares containing a mine.

## Functions
1. Load pre-existing boards
2. Generate random boards
3. Count number of mines that surrounds each square
4. Play game by entering locations
5. Brute-Force to generate solution
5. Exit the game at any time

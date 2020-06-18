# ------------------------------------------------------
#        Name: Chitose Maruko, Marium Tapal, Dianne Caravela and Eleni Partakki
#    Filename: finalproject.py
#     Section: L02
#        Date: 04/24/2019
#  References: We used a video at the end from eviatkin on YouTube, and this gif for when a player loses: https://tenor.com/view/explosion-boom-gif-8911339
# ------------------------------------------------------

Files in our project:
1. main.py
2. block.py
3. functions.py

To run the game, you need to run main.py


How to run our project: To play this game, pick the level of the game you want from Easy, Medium or Hard... or if you make a mistake, expect a spicy answer. Then, pick a row and a column to pick a block, and then you'll decide whether you’d like to Open It or Flag It. To flag, means that you are assuming that there is a bomb in that block but if you open it, you're assuming that there is no bomb and that it is safe to open. If you open a bomb, you lose, but if not, you continue playing until you've flagged all the bombs and opened all the other blocks!


What is Minesweeper: Minesweeper is a game on a square board (9 * 9 Board and 10 Mines)
and we have to pick a row and column on the board for
which we believe there is no mine, and open it.
We don’t know where mines are. If we do think there is a mine,
we should pick the row and column, and flag it!
If a cell where a mine is present is chosen and opened then you lose,
else you are still in the game.'

The goal of the game is: Minesweeper will help people be able to kill time, use their brains and be entertained (and save the world by sweeping mines!!!)


Architecture: We have created a main functions that calls class block, and then we use methods to call particular aspects of our game. The block class holds most of the game, and the main function helps run all aspects of it.

One major challenge we faced and how we overcame it: A major challenge we faced was that we had to decide how we wanted our game to look and its levels of difficulty. To solve the problem, we decided to code a simpler and a harder game to please everyone.


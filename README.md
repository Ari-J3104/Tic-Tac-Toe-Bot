# Tic-Tac-Toe-Bot

This project was created as a pass-time over the summer using Python. My goal was to create a best of 5 tic-tac-toe bot that wasn't smart enough to always win/tie, but could reflect intelligent move choice while in reality being completely made up of conditional statements. 

After each round, the bot will reset the board, however, there is a glitch in which two turns will happen on a cleared board, but then they will get erased and the board will get cleared again. These two moves seem to always happen, and they are needed in order to fully reset the board. I could not find a way to work around this. 

Besides this small glitch, the bot works very well. It randomly choses who goes first each round. 

The inputs should look like this: 00, 01, 02, 10, 11, 12, 20, 21, 22
These represent board spaces by coordinates, where the first number is the row, and the second is the column, so 11 would be the middle square.

00 | 01 | 02
_____________
10 | 11 | 12
_____________
20 | 21 | 22

To run the program, enter "python tictactoe.py" into the commandline.

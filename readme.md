## Riddler Jan 6th 2020

This calculates the highest possible board for the Spelling Bee game.

It solves the 538 Riddler due on January 6th 2020 [https://fivethirtyeight.com/features/can-you-solve-the-vexing-vexillology/](https://fivethirtyeight.com/features/can-you-solve-the-vexing-vexillology/).

First, I loop through each letter in the alphabet, this will be the center letter.

Next, I find each word in the dictionary that is a pangram, and contains this letter. Each of these define a board

Finally, for each board I add up the score of all the letters which are a subset of the letters in the board.

I keep track of the highest scoring board as I loop over each candidate center letter.

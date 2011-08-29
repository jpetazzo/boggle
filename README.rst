Boggle Solver
=============

I don't know if that's the official name of this word game, but that's how
it was called the first time I played it :-)

This small program tries to give you all the words it can find on a 5x5
matrix of letters. Words are valid if they can be made by following a path
of consecutive letters. Paths can go in any possible direction (horizontal,
vertical, diagonal). A path cannot use twice the same matrix position.
If you want to make a word using twice the same letter, the letter has to
be in the matrix multiple times.

To run it:

#. Make sure that you have /usr/share/dict/words (or install it, or change
   the path in the code).
#. Start the program by specifying the 5x5 letter matrix on the command-line,
   e.g. ./boggle.py foqsleisoptiwosbzlqpgoerg

I decided to put this on GitHub because I happen to be rewriting this every
now and then, for the sole purpose of showing some people that they can
indeed be replaced with a tiny script :-)

# Boggle Solver

I don't know if that's the official name of this word game, but that's how
it was called the first time I played it :-)

I decided to put this on GitHub because I happen to be rewriting this every
now and then, for the sole purpose of ~~showing some people that they can
indeed be replaced with a tiny script~~ cheating at word games when matching
against liberal arts majors 😧

There are two versions of the program, but essentially, they work the same
way: you give them a 4x4 or 5x5 letter matrix as input on the command
line, and they output a list of words that can be made from the matrix.

Words are valid if they can be made by following a path
of consecutive letters. Paths can go in any possible direction (horizontal,
vertical, diagonal). A path cannot use twice the same matrix position.
If you want to make a word using twice the same letter, the letter has to
be in the matrix multiple times.

To run it:

#. Make sure that you have /usr/share/dict/words (or install it, or change
   the path in the code).
#. Start the program by specifying the letter matrix on the command-line,
   e.g. `python boggle5.py foqsleisoptiwosbzlqpgoerg`.

The output of boggle5 and boggle4 are different; boggle4 also shows you
how to trace the word.


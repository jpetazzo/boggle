#!/usr/bin/env python
"""
Boggle Solver
=============

#. Make sure that you have /usr/share/dict/words (or install it, or change
   the path in the code).
#. Start the program by specifying the 5x5 letter matrix on the command-line,
   e.g. ./boggle.py foqsleisoptiwosbzlqpgoerg


Algorithm
---------

The program iterates on all positions of the grid, and from each position,
it tries to build all the possible words, by starting a recursive algorithm.

The recursive function is `explore`.

To make word lookups faster, the dictionary is initially loaded in a tree.
The tree is actually an automaton: if a path exists from the root to the "EOW"
(End-Of-Word) final state marker, then the word exists.

The positions are encoded like this::

 0  1  2  3  4
 5  6  7  8  9
 10 11 12 13 14
 15 16 17 18 19
 20 21 22 23 24
"""

# end of word marker (must not be in any word)
EOW = '.'


import sys


def addword(tree, word):
    """Add word to the given tree. Works recursively."""
    if word:
        head, tail = word[0], word[1:]
        # If the first letter of the word is not in the (sub-)tree,
        # create an empty node.
        if head not in tree:
            tree[head] = {}
        # Add the rest of the word to the subtree.
        addword(tree[head], tail)
    else:
        # If we were given the empty word, add a final state in the tree,
        # to note that the path from the root to here is a valid word.
        tree[EOW] = EOW


def buildtree(dictfile):
    """The argument should be a path to a file containing one word per line."""
    tree = dict()
    with open(dictfile) as f:
        for word in f:
            word = word.strip()
            addword(tree, word)
    return tree


def neighbors(pos):
    """Returns all positions around the given position.

    Remember that the game does not take place on a torus; therefore, it's
    not possible to e.g. wrap around the left edge to go to the right edge.

    Note: since this function does not rely on external state, a small speed
    improvement can be obtained by memoizing its output, or just building
    a lookup table on startup.
    """
    top = pos<5
    bottom = pos>19
    left = pos%5==0
    right = pos%5==4

    horizontal = [0]
    if not left:
        horizontal.append(-1)
    if not right:
        horizontal.append(1)

    vertical = [0]
    if not top:
        vertical.append(-5)
    if not bottom:
        vertical.append(5)

    return [pos+h+v
            for h in horizontal
            for v in vertical
            if h and v]


def explore(curword, curtree, nextpos, usedpos, results):
    """Check what word we have so far, and try to make longer words.
    
    * ``curword`` is the word we have so far (as a string);
    * ``curtree`` is the (sub-)tree of possible words (it's a sub-tree
      of the dictionary tree built in the beginning; if ``curword`` is empty,
      it's the whole tree);
    * ``nextpos`` is the number of the position we are about to try to add;
    * ``usedpos`` is the list of positions we used so far;
    * ``results`` is the dictionary of words found so far (the key is the
      word as a string, and the value is the path, kept to later show the
      word on the matrix).
    """
    # Don't try to re-use a position.
    if nextpos in usedpos:
        return
    # Add the tentative position to the list of used positions.
    usedpos.append(nextpos)
    # Lookup the letter on the tentative position.
    nextletter = boggle[nextpos]
    # Check at least one word starts with the letters we got so far.
    if nextletter not in curtree:
        #print 'Cannot make word {0}{1}'.format(curword,nextletter)
        return
    # Build the new tentative prefix.
    nextword = curword+nextletter
    # Lookup the subtree corresponding to the new tentative prefix.
    nexttree = curtree[nextletter]
    # If the tentative prefix is an actual word, remember it.
    if EOW in nexttree:
        if nextword not in results:
            #print 'Found',nextword,usedpos
            results[nextword] = usedpos[:]
    # Lookup all the positions around the current tentative position.
    childrenpos = neighbors(nextpos)
    # Re-run the algorithm for each new tentative position.
    for childpos in childrenpos:
        explore(nextword, nexttree, childpos, usedpos[:], results)
        

boggle = sys.argv[1]
assert len(boggle)==25

wordstree = buildtree("/usr/share/dict/words")

results = dict()
for root in range(25):
    explore('', wordstree, root, list(), results)
results = [(len(word), word, path) for (word,path) in results.items()]
results.sort()
results.reverse()
for l,word,path in results:
    print word
    print 13*'*'
    for line in range(5):
        print '*',
        for col in range(5):
            pos = 5*line+col
            if pos in path:
                print boggle[pos],
            else:
                print ' ',
        print '*',
        print
    print 13*'*'
    raw_input()

for line in range(5):
    for col in range(5):
        print boggle[5*line+col],5*line+col,'\t',
    print

#!/usr/bin/env python
import sys

raw_board = sys.argv[1].lower()
assert len(raw_board) == 16

board = dict(zip([(x,y) for x in range(4) for y in range(4)], raw_board))

def tree_add(tree, word):
    if word == "":
	tree[True] = True
	return
    head, tail = word[0], word[1:]
    if head not in tree:
	tree[head] = {}
    tree_add(tree[head], tail)

def tree_search(tree, word):
    if word == "":
	return tree
    head, tail = word[0], word[1:]
    if head not in tree:
	return {}
    return tree_search(tree[head], tail)

word_tree = {}
for word in open("/usr/share/dict/words"):
    tree_add(word_tree, word.strip().lower())

results = dict()

def explore(list_of_positions):
    word = "".join(board[p] for p in list_of_positions)
    sub_tree = tree_search(word_tree, word)
    if sub_tree == {}:
	return
    if True in sub_tree:
	if len(word) >= 3:
	    results[word] = list_of_positions
    x, y = list_of_positions[-1]
    for (dx, dy) in [ (dx, dy) for dx in [-1, 0, 1] for dy in [ -1, 0, 1] ]:
	nx, ny = x+dx, y+dy
	# New position is out of the board
	if nx not in range(4) or ny not in range(4):
	    continue
	# Do not reuse the same position twice
	if (nx, ny) in list_of_positions:
	    continue
	explore(list_of_positions + [(nx, ny)])

for first_position in [ (x,y) for x in range(4) for y in range(4) ]:
    explore([first_position])

symbol = {
    (-1, -1): "\\",
    (1, 1): "\\",
    (-1, 0): "|",
    (1, 0): "|",
    (0, 1): "-",
    (0, -1): "-",
    (1, -1): "/",
    (-1, 1): "/",
    }

results = results.items()
results.sort(cmp=lambda a,b: -cmp(len(a[0]),len(b[0])))
counter = 0
for word, positions in results:
    counter += 1
    if counter % 5 == 0:
	raw_input()
	print 5*"\n"
    print word
    print
    path = []
    for line in range(7):
	path.append([" ", " ", " ", " ", " ", " ", " "])
    for (x, y) in [ (x, y) for x in range(4) for y in range(4) ]:
	path[2*x][2*y] = "."
    x, y = positions[0]
    path[2*x][2*y] = word[0].upper()
    for pos1, pos2, letter in zip(positions[:-1], positions[1:], word[1:]):
	x1, y1 = pos1
	x2, y2 = pos2
	dx, dy = x2-x1, y2-y1
	path[2*x2][2*y2] = letter
	if path[x1+x2][y1+y2] != " ":
	    path[x1+x2][y1+y2] = "*"
	else:
	    path[x1+x2][y1+y2] = symbol[dx, dy]
    for line in path:
	print "".join(line)
    print 10*"_"
	

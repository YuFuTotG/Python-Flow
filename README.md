## Python-Flow

# Problem:
You are given a nxm grid where some cells are populated by a single colour.
Each colour repeates twice. Want to connect all the colours such that no paths intersect and the grid is entirly filled

# Problem Instance:
A nxm grid of numbers:
	- non-zero: where each non-zero number is repeate twice:
	- zero: representing empty cells

Example Problem Instance:
	00000
	01040
	00400
	00203
	21300

# Problem Solution:
A nxn grid populated by number:
	- Zero entries from problem instance are replaces by non-zero entries.
	- Identical numbers are adjacent to each other.
	- A subgraph of size 2x2 much contain atleast two unique colours.

Example Problem Solution:
	22222
	21442
	21422
	21223
	21333

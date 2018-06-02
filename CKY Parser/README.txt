This project requires python 3.x +

Please use the following command to run the program:
	python nlp_proj.py "grammar_rules_1.txt" "flies like arrows"	
	
---------------------------------------------------------------------------------------------------------

The CKY algorithm is one of the most widely used methods.
One of the most important requirements of the CKY algorithm is that the grammar must be in Chomsky
Normal Form. The right-hand side of each rule must expand either to two non-terminals or a single
terminal. A simple two-dimensional matrix can be used to encode the structure of an entire tree.
Each cell [i, j] contains a set of non-terminals that represent all the constituents that span position I
through j of the input. Since our grammar is in CNF, the non-terminal entries in the table have exactly
two daughters. Thus, for each constituent represented by the entry [i, j] in the table, there must be a
position k, where it can be split into two parts, such that i<k<j.
The first constituent [i, k] must lie to the left of [i, j] and the second constituent must lie beneath it.
CKY recognition is mainly just filling in this table in the correct way. The cells are filled in a bottom-up 
fashion, going from left to right. The CKY algorithm is a recognizer and not a parser. To turn it into a parser, 
we need to add back pointers to each non-terminal to know where it was derived from and allow multiple entries 
of the same nonterminal into the table.

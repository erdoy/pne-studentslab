from Seq1 import *

# -- Create a Null sequence
s = Seq()

FILENAME = "U5.txt"

# -- Initialize the null seq with the given file in fasta format
s.read_fasta(FILENAME)

print_seqs([s])

print("  Bases: " + str(s.count()))
print("  Rev: " + s.reverse())
print("  Comp: " + s.complement())

from Seq1 import *

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

seqs = [s1, s2, s3]

for i in range(len(seqs)):
    print_seqs(seqs, i)

    print("  Bases: " + str(seqs[i].count()))

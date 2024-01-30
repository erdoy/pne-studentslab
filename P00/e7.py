from Seq0 import *

FOLDER = "/home/alumnos/edgamen/Escritorio/PNE/sequences/"
FILENAME = "U5.txt"

seq = seq_read_fasta(FOLDER + FILENAME)[:20]

print("Gene " + FILENAME[:-4] + ":")
print("Frag: " + seq)
print("Comp: " + seq_complement(seq))
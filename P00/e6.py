from Seq0 import *

FOLDER = "/home/alumnos/edgamen/Escritorio/PNE/sequences/"
FILENAME = "U5.txt"

print(seq_read_fasta(FOLDER + FILENAME)[:20])
print(seq_reverse(seq_read_fasta(FOLDER + FILENAME), 20))

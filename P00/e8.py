from Seq0 import *

FOLDER = "/home/alumnos/edgamen/Escritorio/PNE/sequences/"
FILENAMES = ["U5", "ADA", "FRAT1", "FXN"]

for FILENAME in FILENAMES:
    count = seq_count(seq_read_fasta(FOLDER + FILENAME + ".txt"))
    print("Gene " + FILENAME + ": Most frequent base: " + max(count, key=count.get))

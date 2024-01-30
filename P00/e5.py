from Seq0 import *

FOLDER = "/home/alumnos/edgamen/Escritorio/PNE/sequences/"
FILENAMES = ["U5", "ADA", "FRAT1", "FXN"]

for FILENAME in FILENAMES:
    print("Gene " + FILENAME + ":", seq_count(seq_read_fasta(FOLDER + FILENAME + ".txt")))
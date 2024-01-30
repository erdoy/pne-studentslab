from Seq0 import *

FOLDER = "/home/alumnos/edgamen/Escritorio/PNE/sequences/"
FILENAMES = ["U5", "ADA", "FRAT1", "FXN"]

bases = ["A", "C", "T", "G"]

for FILENAME in FILENAMES:
    print("Gene " + FILENAME + ":")
    for base in bases:
        print("  " + base + ":",seq_count_base(seq_read_fasta(FOLDER + FILENAME + ".txt"), base))
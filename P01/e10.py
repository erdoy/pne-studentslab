from Seq1 import *

FOLDER = "/home/alumnos/edgamen/Escritorio/PNE/sequences/"
FILENAMES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

s = Seq()

for i in FILENAMES:
    s.read_fasta(FOLDER + i + ".txt")
    print(f"Gene {i}: Most frequent Base: {str(max(s.count(), key = s.count().get))} ")

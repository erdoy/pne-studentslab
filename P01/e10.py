from Seq1 import *

FOLDER = "/home/alumnos/edgamen/Escritorio/PNE/sequences/"
FILENAMES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

seqs = []

for i in FILENAMES:
    s = Seq()
    s.read_fasta(FOLDER + i + ".txt")
    seqs.append(s)
    print(f"Gene {i}: Most frequent Base: {str(max(s.count(), key = s.count().get))} ")



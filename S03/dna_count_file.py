def filebasecount(filepath):
    seq_len = 0
    bases = {"A": 0,
             "C": 0,
             "G": 0,
             "T": 0}

    with open(filepath, "r", encoding="latin-1") as f:
        for line in f:
            for i in line.replace("\n", ""):
                seq_len += 1
                for j in bases:
                    if i == j:
                        bases[j] += 1

    print("Total length:", seq_len)
    for j in bases:
        print(j + ":", bases[j])


filebasecount("dna.txt")

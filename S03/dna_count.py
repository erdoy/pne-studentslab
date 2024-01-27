def basecount():
    seq = input("Introduce the sequence: ").upper()
    bases = {"A": 0,
             "C": 0,
             "G": 0,
             "T": 0}

    for i in seq:
        for j in bases:
            if i == j:
                bases[j] += 1

    print("Total length:", len(seq))
    for j in bases:
        print(j + ":", bases[j])

basecount()

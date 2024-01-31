class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


def print_seqs(seq_list):
    for i in range(len(seq_list)):
        print("Sequence " + str(i) + ": (Length " + str(seq_list[i].len()) + ") " + str(seq_list[i]))


def generate_seqs(pattern, n):
    seqs = []
    for i in range(1, n + 1):
        seq = pattern * i
        seqs.append(Seq(seq))

    return seqs


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)

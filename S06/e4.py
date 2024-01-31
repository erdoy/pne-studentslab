from termcolor import cprint


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


def print_seqs(seq_list, color):
    for i in range(len(seq_list)):
        cprint("Sequence " + str(i) + ": (Length " + str(seq_list[i].len()) + ") " + str(seq_list[i]), color, force_color=True)


def generate_seqs(pattern, n):
    seqs = []
    for i in range(1, n + 1):
        seq = pattern * i
        seqs.append(Seq(seq))

    return seqs


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print()
cprint("List 1:", "blue", force_color=True)
print_seqs(seq_list1, "blue")

print()
cprint("List 2:", "green", force_color=True)
print_seqs(seq_list2, "green")

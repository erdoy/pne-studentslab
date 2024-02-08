class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        self.valid = False
        self.bases = ["A", "C", "T", "G"]

        if self.strbases == "" or self.strbases == "NULL":
            print("NULL Seq created")
        else:
            self.validate()

            if not self.valid:
                print("INVALID Seq!")
            else:
                print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def validate(self):

        self.strbases = self.strbases.replace("\n", "").upper()
        self.valid = True

        for i in self.strbases:
            if i not in self.bases:
                self.valid = False
                self.strbases = "ERROR"
                break

    def read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        self.strbases = file_contents[file_contents.find("\n"):].replace("\n", "")
        self.validate()

    def len(self):
        """Calculate the length of the sequence"""
        len_val = 0
        if self.valid:
            len_val = len(self.strbases)

        return len_val

    def count_base(self, base):
        value = 0

        if self.valid:
            for i in self.strbases:
                if i == base:
                    value += 1

        return value

    def count(self):
        base_count = dict(zip(self.bases, [0 for i in self.bases]))

        if self.valid:
            for i in self.strbases:
                for j in base_count:
                    if i == j:
                        base_count[j] += 1

        return base_count

    def reverse(self):
        rev = self.strbases

        if self.valid:
            rev = self.strbases[::-1]

        return rev

    def complement(self):
        comp = self.strbases
        comp_bases = {"A": "T", "C": "G", "G": "C", "T": "A"}

        if self.valid:
            comp = ""

            for i in self.strbases:
                comp += comp_bases[i]

        return comp


def print_seqs(seq_list, n=None):
    if type(n) == int:
        print("Sequence " + str(n) + ": (Length " + str(seq_list[n].len()) + ") " + str(seq_list[n]))
    else:
        for i in range(len(seq_list)):
            print("Sequence " + str(i) + ": (Length " + str(seq_list[i].len()) + ") " + str(seq_list[i]))

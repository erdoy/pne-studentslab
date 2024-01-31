class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        if self.strbases == "" or self.strbases == "NULL":
            print("NULL Seq created")
        # elif valid == True:
        #     print()
        else:
            print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


null_seq = Seq()
valid_seq = Seq("ACTGA")

print("Sequence 1:", null_seq)
print("Sequence 2:", valid_seq)

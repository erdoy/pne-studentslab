from pathlib import Path


def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    return file_contents[file_contents.find("\n"):].replace("\n", "")


def seq_len(seq=None):
    return len(seq)


def seq_count_base(seq, base=None):
    count = 0

    for i in seq:
        if i == base:
            count += 1

    return count


def seq_count(seq):
    bases = ["A", "T", "C", "G"]
    count = dict(zip(bases, [0 for i in bases]))

    for j in count:
        count[j] = seq_count_base(seq, j)

    return count


def seq_reverse(seq, n):
    seq = seq[:n]
    return seq[::-1]


def seq_complement(seq):
    complements = {"A": "T", "C": "G", "T": "A", "G": "C"}
    complement_seq = ""

    for i in seq:
        complement_seq += complements[i]

    return complement_seq
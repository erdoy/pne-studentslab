from pathlib import Path


def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    return file_contents[file_contents.find("\n"):].replace("\n", "")


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
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
    return "hhhhh"


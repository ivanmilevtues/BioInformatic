def count_nucleotides(data_set):
    nucleotides = {
        'A': 0,
        'G': 0,
        'C': 0,
        'T': 0
    }

    for nucleotide in data_set:
        try:
            nucleotides[nucleotide] += 1
        except KeyError:
            print('Unknown nucleotide')

    return nucleotides


def main():
    data_set = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

    nucleotides = count_nucleotides(data_set)
    print("{} {} {} {}".format(nucleotides['A'], nucleotides['C'],
                            nucleotides['G'], nucleotides['T']))

if __name__ == "__main__":
    main()

def complement(data_set):
    match_key = {
        'G': 'C',
        'A': 'T',
        'T': 'A',
        'C': 'G'
    }
    result = ''
    for ch in data_set:
        result += match_key[ch]
    return result[::-1]

def main():
    data_set = "AAAACCCGGT"
    print(complement(data_set))


if __name__ == '__main__':
    main()
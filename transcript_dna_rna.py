def transcript(data_set):
    match_key = {
        'G': 'G',
        'A': 'A',
        'T': 'U',
        'C': 'C'
    }
    result = ''
    for ch in data_set:
        result += match_key[ch]
    return result


def main():
    data_set = "GATGGAACTTGACTACGTAAATT"
    print(transcript(data_set))


if __name__ == '__main__':
    main()
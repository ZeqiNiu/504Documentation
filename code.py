"""20200826-BIOINF504 Exercise code"""
def count_nuc(input_nuc):
    b = dict()
    for c in input_nuc:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b
"""Prints the counts of each nucleotide"""
def freq_nuc(input_nuc):
    print('freqs')
    total = float(sum([input_nuc[b] for b in input_nuc.keys()]))
    for b in input_nuc.keys():
        print(b + ':' + str(input_nuc[b]/total))
"""caculates the frequency
of each nucleotide"""
freq_nuc(count_nuc('ATCTGACGCGCGCCGC'))




def get_char_relFreq(char_array):
    """ A function to return relative frequency
    for each character in the character array.
    Args:
        - char_array (str): character array
    Returns:
        - relative_freqs (dict): keys are unique characters, values are counts
    """
    relative_freqs = {}
    total = len(char_array)
    for _char in set(char_array):
        relative_frequnecy = char_array.count(_char) / total
        relative_freqs[_char] = relative_frequnecy
    return relative_freqs
print(get_char_relFreq('ATCTGACGCGCGCCGC'))
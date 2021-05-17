import tensorflow as tf
import numpy as np
np.random.seed(0)

# ID_TO_SMILES_CHARACTER = {0: ' ',
#                           1: '(',
#                           2: ')',
#                           3: '*',
#                           4: '+',
#                           5: '-',
#                           6: '1',
#                           7: '2',
#                           8: '3',
#                           9: '4',
#                           10: '5',
#                           11: '=',
#                           12: 'C',
#                           13: 'H',
#                           14: 'N',
#                           15: 'O',
#                           16: 'P',
#                           17: 'S',
#                           18: '[',
#                           19: ']',
#                           20: 'c',
#                           21: 'n',
#                           22: 'o'}
#
# SMILES_CHARACTER_TO_ID = {' ': 0,
#                           '(': 1,
#                           ')': 2,
#                           '*': 3,
#                           '+': 4,
#                           '-': 5,
#                           '1': 6,
#                           '2': 7,
#                           '3': 8,
#                           '4': 9,
#                           '5': 10,
#                           '=': 11,
#                           'C': 12,
#                           'H': 13,
#                           'N': 14,
#                           'O': 15,
#                           'P': 16,
#                           'S': 17,
#                           '[': 18,
#                           ']': 19,
#                           'c': 20,
#                           'n': 21,
#                           'o': 22}

# ID_TO_AMINO_ACID = {0: '0',
#                     1: 'A',
#                     2: 'C',
#                     3: 'D',
#                     4: 'E',
#                     5: 'F',
#                     6: 'G',
#                     7: 'H',
#                     8: 'I',
#                     9: 'K',
#                     10: 'L',
#                     11: 'M',
#                     12: 'N',
#                     13: 'P',
#                     14: 'Q',
#                     15: 'R',
#                     16: 'S',
#                     17: 'T',
#                     18: 'V',
#                     19: 'W',
#                     20: 'Y'}
#
# AMINO_ACID_TO_ID = {'0': 0,
#                     'A': 1,
#                     'C': 2,
#                     'D': 3,
#                     'E': 4,
#                     'F': 5,
#                     'G': 6,
#                     'H': 7,
#                     'I': 8,
#                     'K': 9,
#                     'L': 10,
#                     'M': 11,
#                     'N': 12,
#                     'P': 13,
#                     'Q': 14,
#                     'R': 15,
#                     'S': 16,
#                     'T': 17,
#                     'V': 18,
#                     'W': 19,
#                     'Y': 20}

# ID_TO_AMINO_ACID = {0: '0',
#                     1: 'A',
#                     2: 'C',
#                     3: 'T',
#                     4: 'G'}
#
# AMINO_ACID_TO_ID = {'0': 0,
#                     'A': 1,
#                     'C': 2,
#                     'T': 3,
#                     'G': 4}

all_permutations = list(product(["A", "T", "C", "G", "0"], repeat=3))
tuple_codon_permutations = list(filter(lambda i: i[1] != "0", all_permutations))
tuple_codon_permutations = list(
    filter(lambda x: not (x[0] == "0" and x[-1] == "0"), codon_permutations)
)

codon_permutations = []
for i in tuple_codon_permutations:
    codon_permutations.append("".join(i))

codon_permutations.insert(0, '000')

ID_TO_AMINO_ACID = {}
for i in range(len(codon_permutations)):
    ID_TO_AMINO_ACID[i] = codon_permutations[i]

AMINO_ACID_TO_ID = {}
for i in range(len(codon_permutations)):
    AMINO_ACID_TO_ID[codon_permutations[i]] = i

NON_STANDARD_AMINO_ACIDS = ['B', 'O', 'U', 'X', 'Z', 'J']


# def get_lesk_color_mapping():
#     """http://www.bioinformatics.nl/~berndb/aacolour.html
#     Args:
#
#     Returns:
#          amino acid color mapping
#     """
#     return tf.cast(tf.constant([
#         [0, 0, 0],  # 0 - black - 0
#         [255, 255, 255],  # A - White 0,0,0 - 1
#         [255, 255, 0],  # C - Yellow 255,255,0 - 2
#         [255, 0, 0],  # D - Red - 3
#         [255, 0, 0],  # E - Red - 4
#         [255, 0, 255],  # F - Magenta 255, 0, 255 - 5
#         [139, 69, 19],  # G - Brown 139,69,19 - 6
#         [0, 0, 255],  # H - Blue 0, 0, 255 - 7
#         [255, 255, 255],  # I - White 0,0,0 - 8
#         [0, 0, 255],  # K - Blue - 9
#         [255, 255, 255],  # L - White 0,0,0 - 10
#         [255, 255, 255],  # M - White 0,0,0 - 11
#         [0, 255, 0],  # N - Green 0, 255, 0 - 12
#         [139, 69, 19],  # P - Brown 139,69,19 -13
#         [0, 255, 0],  # Q - Green 0, 255, 0 - 14
#         [0, 0, 255],  # R - Blue - 15
#         [0, 255, 0],  # S - Green 0, 255, 0 - 16
#         [0, 255, 0],  # T - Green 0, 255, 0 - 17
#         [255, 255, 255],  # V - White 0,0,0 - 18
#         [255, 0, 255],  # W - Magenta 255, 0, 255 - 19
#         [255, 0, 255],  # Y - Magenta 255, 0, 255 - 20
#
#     ]), tf.float32)

colors = []
for i in range(len(codon_permutations)):
    colors.append(list(np.random.choice(range(256), size=3)))

def get_lesk_color_mapping():
    """
    Args:

    Returns:
         amino acid color mapping
    """
    return tf.cast(tf.constant(colors), tf.float32)

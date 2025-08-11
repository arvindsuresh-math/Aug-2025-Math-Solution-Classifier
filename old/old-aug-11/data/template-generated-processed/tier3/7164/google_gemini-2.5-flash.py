from fractions import Fraction

def solve():
    """Index: 7164.
    Returns: the total number of missing keys on James' keyboard.
    """
    # L1
    total_consonants = 21 # 21 consonants in the alphabet
    missing_consonant_fraction = Fraction(1, 7) # 1/7 of the consonants
    missing_consonants = total_consonants * missing_consonant_fraction

    # L2
    missing_vowels = 2 # two vowels
    total_missing_keys = missing_consonants + missing_vowels

    # FA
    answer = total_missing_keys
    return answer
from fractions import Fraction

def solve():
    """Index: 1783.
    Returns: the total number of conch shells they all have.
    """
    # L1
    david_shells = 15 # If David has 15 shells
    mia_multiplier = 4 # 4 times as many shells as David
    mia_shells = mia_multiplier * david_shells

    # L2
    ava_additional_shells = 20 # 20 more shells than Mia
    ava_shells = mia_shells + ava_additional_shells

    # L3
    alice_fraction = Fraction(1, 2) # half the number of shells Ava has
    alice_shells = alice_fraction * ava_shells

    # L4
    total_shells = david_shells + mia_shells + ava_shells + alice_shells

    # FA
    answer = total_shells
    return answer
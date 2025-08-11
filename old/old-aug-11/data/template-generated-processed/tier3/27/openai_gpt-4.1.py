from fractions import Fraction

def solve():
    """Index: 27.
    Returns: the total number of valuable files Brennan was left with after deleting unrelated files in both rounds.
    """
    # L1
    first_round_total = 800 # After downloading 800 files
    first_round_delete_percent = Fraction(70, 100) # deleted 70% of them
    first_round_non_valuable = first_round_delete_percent * first_round_total

    # L2
    first_round_valuable = first_round_total - first_round_non_valuable

    # L3
    second_round_total = 400 # downloaded 400 more files
    second_round_delete_fraction = Fraction(3, 5) # 3/5 of them were irrelevant
    second_round_non_valuable = second_round_delete_fraction * second_round_total

    # L4
    second_round_valuable = second_round_total - second_round_non_valuable

    # L5
    total_valuable = second_round_valuable + first_round_valuable

    # FA
    answer = total_valuable
    return answer
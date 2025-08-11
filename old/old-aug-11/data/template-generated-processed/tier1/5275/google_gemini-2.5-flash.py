def solve():
    """Index: 5275.
    Returns: the number of stamps Peggy needs to add to her collection to match Bert's.
    """
    # L1
    ernie_multiplier = 3 # three times as many stamps as Peggy
    peggy_stamps = 75 # Peggy currently has 75 stamps
    ernie_stamps = ernie_multiplier * peggy_stamps

    # L2
    bert_multiplier = 4 # four times as many stamps as Ernie
    bert_stamps = bert_multiplier * ernie_stamps

    # L3
    stamps_needed_by_peggy = bert_stamps - peggy_stamps

    # FA
    answer = stamps_needed_by_peggy
    return answer
def solve():
    """Index: 1852.
    Returns: the number of days it will take Bert to have the same number of kangaroos as Kameron.
    """
    # L1
    kameron_kangaroos = 100 # Kameron has 100 kangaroos
    bert_kangaroos = 20 # Bert has 20 kangaroos
    difference_kangaroos = kameron_kangaroos - bert_kangaroos

    # L2
    daily_purchase_rate = 2 # rate of 2 new kangaroos per day
    days_to_match = difference_kangaroos / daily_purchase_rate

    # FA
    answer = days_to_match
    return answer
def solve():
    """Index: 1162.
    Returns: the number of children in the family.
    """
    # L1
    total_granola_bars = 200 # Monroe made 200 granola bars
    eaten_by_adults = 80 # She and her husband ate 80
    granola_bars_for_children = total_granola_bars - eaten_by_adults

    # L2
    bars_per_child = 20 # Each child received 20 granola bars
    number_of_children = granola_bars_for_children / bars_per_child

    # FA
    answer = number_of_children
    return answer
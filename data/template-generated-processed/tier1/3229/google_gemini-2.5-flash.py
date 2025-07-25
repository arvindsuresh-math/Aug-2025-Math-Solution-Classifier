def solve():
    """Index: 3229.
    Returns: the number of more cups Carl sold than Stanley in 3 hours.
    """
    # L1
    stanley_cups_per_hour = 4 # 4 cups of lemonade an hour
    hours = 3 # in 3 hours
    stanley_total_cups = stanley_cups_per_hour * hours

    # L2
    carl_cups_per_hour = 7 # 7 cups of lemonade an hour
    carl_total_cups = carl_cups_per_hour * hours

    # L3
    difference_in_cups = carl_total_cups - stanley_total_cups

    # FA
    answer = difference_in_cups
    return answer
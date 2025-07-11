def solve():
    """Index: 215.
    Returns: the number of children more than adults in the church.
    """
    # L1
    total_members = 120 # A church has 120 members
    adult_percent_decimal = 0.4 # 40% are adults
    num_adults = total_members * adult_percent_decimal

    # L2
    total_percent = 100 # WK
    adult_percent = 40 # 40% are adults
    child_percent = total_percent - adult_percent

    # L3
    child_percent_decimal = 0.6 # .6 from 60%
    num_children = total_members * child_percent_decimal

    # L4
    difference = num_children - num_adults

    # FA
    answer = difference
    return answer
def solve():
    """Index: 215.
    Returns: the number of more children than adults.
    """
    # L1
    total_members = 120 # A church has 120 members
    adult_percentage_decimal = 0.4 # 40% are adults
    num_adults = total_members * adult_percentage_decimal

    # L2
    total_percentage = 100 # WK
    adult_percentage_value = 40 # 40% are adults
    children_percentage_value = total_percentage - adult_percentage_value

    # L3
    children_percentage_decimal = 0.6 # The rest are children (derived from 60%)
    num_children = total_members * children_percentage_decimal

    # L4
    difference_children_adults = num_children - num_adults

    # FA
    answer = difference_children_adults
    return answer
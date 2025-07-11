def solve():
    """Index: 323.
    Returns: the total amount Jay and Gloria would spend at the craft store.
    """
    # L1
    jay_guests = 22 # Jay invited 22 people
    gloria_guests = 36 # Gloria invited 36 people
    total_guests = jay_guests + gloria_guests

    # L2
    jay_flags = 1 # Jay wanted 1 flag
    gloria_flags = 1 # Gloria wanted 1 flag
    total_flags = jay_flags + gloria_flags + total_guests

    # L3
    flags_per_dollar = 5 # 5 flags for $1.00
    total_cost = total_flags / flags_per_dollar

    # FA
    answer = total_cost
    return answer
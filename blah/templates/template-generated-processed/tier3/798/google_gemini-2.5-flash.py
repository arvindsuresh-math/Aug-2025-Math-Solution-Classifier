def solve():
    """Index: 798.
    Returns: the number of additional dozen appetizers Patsy needs to make.
    """
    # L1
    appetizers_per_guest = 6 # 6 appetizers per each
    num_guests = 30 # 30 guests
    total_appetizers_needed = appetizers_per_guest * num_guests

    # L2
    deviled_eggs_dozens = 3 # 3 dozen deviled eggs
    pigs_in_blanket_dozens = 2 # 2 dozen pigs in a blanket
    kebabs_dozens = 2 # 2 dozen kebabs
    appetizers_made_dozens = deviled_eggs_dozens + pigs_in_blanket_dozens + kebabs_dozens

    # L3
    dozen = 12 # WK
    appetizers_made_total = appetizers_made_dozens * dozen

    # L4
    appetizers_remaining_needed = total_appetizers_needed - appetizers_made_total

    # L5
    dozens_more_needed = appetizers_remaining_needed / dozen

    # FA
    answer = dozens_more_needed
    return answer
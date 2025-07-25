def solve():
    """Index: 4157.
    Returns: the total cups of flour Lady Bird will need.
    """
    # L1
    num_members = 18 # 18 members
    biscuits_per_guest = 2 # 2 biscuits per guest
    total_biscuits_needed = num_members * biscuits_per_guest

    # L2
    biscuits_per_batch = 9 # 9 biscuits
    num_batches = total_biscuits_needed / biscuits_per_batch

    # L3
    flour_per_batch = 1.25 # 1 1/4 cup flour
    total_flour_needed = flour_per_batch * num_batches

    # FA
    answer = total_flour_needed
    return answer
def solve():
    """Index: 5614.
    Returns: the total number of blocks Jules has to walk the dogs.
    """
    # L1
    vacation_cost = 1000 # The vacation costs $1,000
    num_family_members = 5 # five members in his family
    amount_per_member = vacation_cost / num_family_members

    # L2
    num_dogs_walked = 20 # walks 20 dogs
    charge_per_start = 2 # charges $2 to start a walk
    earnings_from_start = num_dogs_walked * charge_per_start

    # L3
    remaining_to_earn_from_distance = amount_per_member - earnings_from_start

    # L4
    charge_per_block = 1.25 # $1.25 per block
    total_blocks_to_walk = remaining_to_earn_from_distance / charge_per_block

    # FA
    answer = total_blocks_to_walk
    return answer
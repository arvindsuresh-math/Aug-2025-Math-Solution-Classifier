def solve():
    """Index: 11.
    Returns: the number of driveways Tobias shoveled.
    """
    # L1
    shoes_cost = 95 # costs $95
    change_after_shoes = 15 # has $15 in change
    total_saved = shoes_cost + change_after_shoes

    # L2
    months_saving = 3 # past three months
    allowance_per_month = 5 # $5 allowance a month
    saved_from_allowance = months_saving * allowance_per_month

    # L3
    lawns_mowed = 4 # mows 4 lawns
    lawn_mowing_charge = 15 # $15 to mow a lawn
    earned_from_lawns = lawns_mowed * lawn_mowing_charge

    # L4
    earned_from_driveways = total_saved - earned_from_lawns - saved_from_allowance

    # L5
    shoveling_charge = 7 # $7 to shovel
    num_driveways_shoveled = earned_from_driveways / shoveling_charge

    # FA
    answer = num_driveways_shoveled
    return answer
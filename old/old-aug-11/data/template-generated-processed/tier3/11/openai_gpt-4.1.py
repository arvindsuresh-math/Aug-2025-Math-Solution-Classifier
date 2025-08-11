def solve():
    """Index: 11.
    Returns: the number of driveways Tobias shoveled.
    """
    # L1
    shoe_cost = 95 # costs $95
    change_left = 15 # he has $15 in change
    total_saved = shoe_cost + change_left

    # L2
    months_saving = 3 # past three months
    monthly_allowance = 5 # $5 allowance a month
    allowance_total = months_saving * monthly_allowance

    # L3
    lawns_mowed = 4 # mows 4 lawns
    mow_charge = 15 # charges $15 to mow a lawn
    mowing_earnings = lawns_mowed * mow_charge

    # L4
    shoveling_earnings = total_saved - mowing_earnings - allowance_total

    # L5
    shoveling_charge = 7 # charges $7 to shovel
    driveways_shoveled = shoveling_earnings / shoveling_charge

    # FA
    answer = driveways_shoveled
    return answer
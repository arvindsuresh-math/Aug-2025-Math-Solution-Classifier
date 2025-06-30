def solve(
    shoe_cost: int = 95, # costs $95
    saving_months: int = 3, # for the past three months
    allowance_per_month: int = 5, # gets a $5 allowance a month
    lawn_mowing_charge: int = 15, # charges $15 to mow a lawn
    shoveling_charge: int = 7, # $7 to shovel
    mowed_lawns: int = 4, # mows 4 lawns
    change_left: int = 15 # has $15 in change
):
    """Index: 11.
    Returns: the number of driveways shoveled.
    """
    #: L1
    total_saved = shoe_cost + change_left # eval: 110 = 95 + 15
    #: L2
    allowance_saved = saving_months * allowance_per_month # eval: 15 = 3 * 5
    #: L3
    lawn_mowing_earnings = mowed_lawns * lawn_mowing_charge # eval: 60 = 4 * 15
    #: L4
    shoveling_earnings = total_saved - lawn_mowing_earnings - allowance_saved # eval: 35 = 110 - 60 - 15
    #: L5
    driveways_shoveled = shoveling_earnings / shoveling_charge # eval: 5.0 = 35 / 7
    answer = driveways_shoveled # FINAL ANSWER # eval: 5.0 = 5.0 # FINAL ANSWER
    return answer # eval: return 5.0
def solve(
    shoe_cost: int = 95,  # shoes cost $95
    months_saving: int = 3,  # saving for 3 months
    monthly_allowance: int = 5,  # $5 allowance per month
    mow_lawn_charge: int = 15,  # $15 to mow a lawn
    shovel_driveway_charge: int = 7,  # $7 to shovel a driveway
    change_after_purchase: int = 15,  # $15 in change after buying shoes
    lawns_mowed: int = 4  # mowed 4 lawns
):
    """Index: 11.
    Returns: the number of driveways shoveled.
    """

    #: L1
    total_saved = shoe_cost + change_after_purchase

    #: L2
    total_allowance = months_saving * monthly_allowance

    #: L3
    total_mowing_earnings = lawns_mowed + mow_lawn_charge

    #: L4
    total_shoveling_earnings = total_saved - total_mowing_earnings - total_allowance

    #: L5
    driveways_shoveled = total_shoveling_earnings / shovel_driveway_charge

    #: FA
    answer = driveways_shoveled
    return answer
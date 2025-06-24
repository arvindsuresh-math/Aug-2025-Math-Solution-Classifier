def solve(
        shoes_cost: int = 95, # costs $95
        months_saving: int = 3, # for the past three months
        allowance_per_month: int = 5, # He gets a $5 allowance a month
        lawn_mowing_charge: int = 15, # He charges $15 to mow a lawn
        driveway_shoveling_charge: int = 7, # and $7 to shovel
        change_after_purchase: int = 15, # he has $15 in change
        lawns_mowed: int = 4 # If he mows 4 lawns
    ):
    """Index: 11.
    Returns: the number of driveways Tobias shoveled.
    """
    #: L1
    total_money_saved = shoes_cost + change_after_purchase

    #: L2
    money_from_allowance = months_saving * allowance_per_month

    #: L3
    money_from_mowing_lawns = lawns_mowed * lawn_mowing_charge

    #: L4
    money_from_shoveling_driveways = total_money_saved - money_from_mowing_lawns - money_from_allowance

    #: L5
    num_driveways_shoveled = money_from_shoveling_driveways / driveway_shoveling_charge

    answer = num_driveways_shoveled # FINAL ANSWER
    return answer
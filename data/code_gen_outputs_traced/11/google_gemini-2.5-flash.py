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
    total_money_saved = shoes_cost + change_after_purchase # eval: 110 = 95 + 15

    #: L2
    money_from_allowance = months_saving * allowance_per_month # eval: 15 = 3 * 5

    #: L3
    money_from_mowing_lawns = lawns_mowed * lawn_mowing_charge # eval: 60 = 4 * 15

    #: L4
    money_from_shoveling_driveways = total_money_saved - money_from_mowing_lawns - money_from_allowance # eval: 35 = 110 - 60 - 15

    #: L5
    num_driveways_shoveled = money_from_shoveling_driveways / driveway_shoveling_charge # eval: 5.0 = 35 / 7

    #: FA
    answer = num_driveways_shoveled # eval: 5.0 = 5.0
    return answer # eval: return 5.0

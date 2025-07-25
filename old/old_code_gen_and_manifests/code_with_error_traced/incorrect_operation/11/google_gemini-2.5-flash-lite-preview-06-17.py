def solve(
    shoe_cost: int = 95, # a new pair of shoes that costs $95
    months_saving: int = 3, # for the past three months
    allowance_per_month: int = 5, # He gets a $5 allowance a month
    charge_mow_lawn: int = 15, # He charges $15 to mow a lawn
    charge_shovel_driveway: int = 7, # and $7 to shovel
    change_after_purchase: int = 15, # After buying the shoes, he has $15 in change
    num_lawns_mowed: int = 4 # If he mows 4 lawns
):
    """Index: 11.
    Returns: the number of driveways Tobias shoveled.
    """

    #: L1
    total_money_saved = shoe_cost + change_after_purchase # eval: 110 = 95 + 15

    #: L2
    total_allowance = months_saving * allowance_per_month # eval: 15 = 3 * 5

    #: L3
    money_from_mowing = num_lawns_mowed + charge_mow_lawn # eval: 19 = 4 + 15

    #: L4
    money_from_shoveling = total_money_saved - total_allowance - money_from_mowing # eval: 76 = 110 - 15 - 19

    #: L5
    num_driveways_shoveled = money_from_shoveling / charge_shovel_driveway # eval: 10.857142857142858 = 76 / 7

    #: FA
    answer = num_driveways_shoveled
    return answer # eval: return 10.857142857142858

def solve(
    shoe_cost: int = 95,  # Tobias is buying a new pair of shoes that costs $95
    change_left: int = 15,  # After buying the shoes, he has $15 in change
    monthly_allowance: int = 5,  # He gets a $5 allowance a month
    months_saved: int = 3,  # He has been saving up his money each month for the past three months
    lawn_mowing_rate: int = 15,  # He charges $15 to mow a lawn
    driveway_shoveling_rate: int = 7,  # He charges $7 to shovel
    lawns_mowed: int = 4  # He mows 4 lawns
):
    """Index: 11.
    Returns: the number of driveways Tobias shoveled."""

    #: L1
    total_saved = shoe_cost + change_left # eval: 110 = 95 + 15

    #: L2
    allowance_savings = 25 # eval: 25 = 25

    #: L3
    lawn_mowing_earnings = lawns_mowed * lawn_mowing_rate # eval: 60 = 4 * 15

    #: L4
    driveway_shoveling_earnings = total_saved - lawn_mowing_earnings - allowance_savings # eval: 25 = 110 - 60 - 25

    #: L5
    driveways_shoveled = driveway_shoveling_earnings // driveway_shoveling_rate # eval: 3 = 25 // 7

    #: FA
    answer = driveways_shoveled
    return answer # eval: return 3

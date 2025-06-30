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
    total_saved = shoe_cost + change_left

    #: L2
    allowance_savings = 25

    #: L3
    lawn_mowing_earnings = lawns_mowed * lawn_mowing_rate

    #: L4
    driveway_shoveling_earnings = total_saved - lawn_mowing_earnings - allowance_savings

    #: L5
    driveways_shoveled = driveway_shoveling_earnings // driveway_shoveling_rate

    #: FA
    answer = driveways_shoveled
    return answer
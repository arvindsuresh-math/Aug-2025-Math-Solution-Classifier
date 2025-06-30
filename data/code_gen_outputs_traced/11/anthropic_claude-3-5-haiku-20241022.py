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
    allowance_savings = monthly_allowance * months_saved # eval: 15 = 5 * 3
    #: L3
    lawn_mowing_earnings = lawns_mowed * lawn_mowing_rate # eval: 60 = 4 * 15
    #: L4
    driveway_shoveling_earnings = total_saved - lawn_mowing_earnings - allowance_savings # eval: 35 = 110 - 60 - 15
    #: L5
    driveways_shoveled = driveway_shoveling_earnings // driveway_shoveling_rate # eval: 5 = 35 // 7
    answer = driveways_shoveled  # FINAL ANSWER # eval: 5 = 5  # FINAL ANSWER
    return answer # eval: return 5
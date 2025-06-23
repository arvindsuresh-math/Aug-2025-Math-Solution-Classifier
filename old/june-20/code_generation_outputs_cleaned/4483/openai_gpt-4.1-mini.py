def solve(
    total_records: int = 200  # Peggy has 200 records
):
    """Index: 4483.
    Returns: the difference in profit between Sammy's and Bryan's deals.
    """
    #: L1
    sammy_offer = total_records * 4

    #: L2
    half_records = total_records / 2

    #: L3
    bryan_offer_interested = half_records * 6

    #: L4
    bryan_offer_not_interested = half_records * 1

    #: L5
    bryan_total_offer = bryan_offer_interested + bryan_offer_not_interested

    #: L6
    profit_difference = sammy_offer - bryan_total_offer

    answer = profit_difference  # FINAL ANSWER
    return answer
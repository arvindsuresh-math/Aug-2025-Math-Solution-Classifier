def solve(
    sammy_price: int = 4,  # "buy all of them for 4 dollars each"
    bryan_interest_price: int = 6,  # "offer 6 dollars each for the half that he is interested in"
    bryan_other_price: int = 1,  # "1 dollar each for the remaining half"
    total_records: int = 200  # "Peggy has 200 records"
):
    """Index: 4483.
    Returns: the difference in profit between Sammy and Bryan's deal.
    """
    #: L1
    sammy_total = total_records * sammy_price

    #: L2
    half_records = total_records / 2

    #: L3
    bryan_first_half = half_records * bryan_interest_price

    #: L4
    bryan_second_half = half_records * bryan_other_price

    #: L5
    bryan_total = bryan_first_half + bryan_second_half

    #: L6
    profit_difference = sammy_total - bryan_total

    answer = profit_difference  # FINAL ANSWER
    return answer
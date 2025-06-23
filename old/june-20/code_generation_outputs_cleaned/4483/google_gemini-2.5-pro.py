def solve(
    sammy_price_per_record: int = 4, # Sammy says that he will buy all of them for 4 dollars each
    bryan_price_per_record_interested: int = 6, # offer 6 dollars each for the half that he is interested in
    bryan_price_per_record_not_interested: int = 1, # and 1 dollar each for the remaining half
    num_records: int = 200 # If Peggy has 200 records
):
    """Index: 4483.
    Returns: the difference in profit between Sammy's and Bryan's deals.
    """
    #: L1
    sammy_total_offer = num_records * sammy_price_per_record

    #: L2
    half_records = num_records / 2

    #: L3
    bryan_offer_first_half = half_records * bryan_price_per_record_interested

    #: L4
    bryan_offer_second_half = half_records * bryan_price_per_record_not_interested

    #: L5
    bryan_total_offer = bryan_offer_first_half + bryan_offer_second_half

    #: L6
    profit_difference = sammy_total_offer - bryan_total_offer

    answer = profit_difference # FINAL ANSWER
    return answer
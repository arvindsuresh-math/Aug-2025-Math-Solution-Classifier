def solve(
    sammy_offer_per_record: int = 4, # Sammy says that he will buy all of them for 4 dollars each.
    bryan_offer_interested_half: int = 6, # will offer 6 dollars each for the half that he is interested in
    bryan_offer_uninterested_half: int = 1, # and 1 dollar each for the remaining half that he is not interested in
    total_records: int = 200 # Peggy has 200 records
):
    """Index: 4483.
    Returns: the difference in profit between Sammy versus Bryan's deal.
    """
    #: L1
    sammy_total_offer = total_records * sammy_offer_per_record

    #: L2
    records_per_half = total_records / 2

    #: L3
    bryan_offer_first_half = records_per_half * bryan_offer_interested_half

    #: L4
    bryan_offer_second_half = records_per_half * bryan_offer_uninterested_half

    #: L5
    bryan_total_offer = bryan_offer_first_half + bryan_offer_second_half

    #: L6
    difference_in_profit = sammy_total_offer - bryan_total_offer

    answer = difference_in_profit  # FINAL ANSWER
    return answer
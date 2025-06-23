def solve(
        sammy_price_per_record: int = 4, # for 4 dollars each
        bryan_fraction_interested: float = 1/2, # half of the records
        bryan_price_interested: int = 6, # 6 dollars each for the half that he is interested in
        bryan_price_not_interested: int = 1, # 1 dollar each for the remaining half that he is not interested in
        total_records: int = 200 # Peggy has 200 records
    ):
    """Index: 4483.
    Returns: the difference in profit between Sammy versus Bryan's deal.
    """
    #: L1
    sammy_profit = total_records * sammy_price_per_record

    #: L2
    records_half = total_records * bryan_fraction_interested

    #: L3
    bryan_profit_interested_half = records_half * bryan_price_interested

    #: L4
    bryan_profit_not_interested_half = records_half * bryan_price_not_interested

    #: L5
    bryan_total_profit = bryan_profit_interested_half + bryan_profit_not_interested_half

    #: L6
    profit_difference = sammy_profit - bryan_total_profit

    answer = profit_difference # FINAL ANSWER
    return answer
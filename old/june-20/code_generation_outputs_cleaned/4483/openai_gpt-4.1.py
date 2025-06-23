def solve(
    price_per_record_sammy: int = 4, # Sammy says that he will buy all of them for 4 dollars each
    price_per_record_bryan_interested: int = 6, # Bryan will offer 6 dollars each for the half that he is interested in
    price_per_record_bryan_not_interested: int = 1, # and 1 dollar each for the remaining half that he is not interested in
    total_records: int = 200 # Peggy has 200 records
):
    """Index: 4483.
    Returns: the difference in profit between Sammy's and Bryan's deals for Peggy's record collection.
    """
    #: L1
    sammy_total = total_records * price_per_record_sammy

    #: L2
    bryan_half = total_records / 2

    #: L3
    bryan_interested_total = bryan_half * price_per_record_bryan_interested

    #: L4
    bryan_not_interested_total = bryan_half * price_per_record_bryan_not_interested

    #: L5
    bryan_total = bryan_interested_total + bryan_not_interested_total

    #: L6
    profit_difference = sammy_total - bryan_total

    answer = profit_difference # FINAL ANSWER
    return answer
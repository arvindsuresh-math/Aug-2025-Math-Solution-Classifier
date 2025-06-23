def solve(
    price_sammy: int = 4, # Sammy says that he will buy all of them for 4 dollars each
    fraction_records_bryan: float = 1/2, # Bryan is only interested in half of the records
    price_interested: int = 6, # will offer 6 dollars each for the half that he is interested in
    price_not_interested: int = 1, # and 1 dollar each for the remaining half that he is not interested in
    total_records: int = 200 # Peggy has 200 records
):
    """Index: 4483.
    Returns: the difference in profit between Sammy's and Bryan's deals."""
    #: L1
    profit_sammy = total_records * price_sammy
    #: L2
    half_records = total_records * fraction_records_bryan
    #: L3
    profit_first_half = half_records * price_interested
    #: L4
    profit_second_half = half_records * price_not_interested
    #: L5
    profit_bryan = profit_first_half + profit_second_half
    #: L6
    difference = profit_sammy - profit_bryan
    answer = difference # FINAL ANSWER
    return answer
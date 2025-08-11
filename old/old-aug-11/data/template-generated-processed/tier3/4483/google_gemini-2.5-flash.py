def solve():
    """Index: 4483.
    Returns: the difference in profit between Sammy's and Bryan's deals.
    """
    # L1
    total_records = 200 # Peggy has 200 records
    sammy_price_per_record = 4 # 4 dollars each
    sammy_total_profit = total_records * sammy_price_per_record

    # L2
    half_divisor = 2 # half of the records
    half_records = total_records / half_divisor

    # L3
    bryan_interested_price = 6 # 6 dollars each for the half that he is interested in
    bryan_interested_profit = half_records * bryan_interested_price

    # L4
    bryan_other_half_price = 1 # 1 dollar each for the remaining half
    bryan_other_half_profit = half_records * bryan_other_half_price

    # L5
    bryan_total_profit = bryan_interested_profit + bryan_other_half_profit

    # L6
    profit_difference = sammy_total_profit - bryan_total_profit

    # FA
    answer = profit_difference
    return answer
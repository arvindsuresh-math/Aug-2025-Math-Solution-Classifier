def solve():
    """Index: 6410.
    Returns: how much cheaper M-Mobile is than T-Mobile.
    """
    # L1
    tmobile_cost_additional_line = 16 # $16 for each additional line
    num_additional_lines = 3 # 5 cell phone lines total - 2 first lines = 3 additional lines
    tmobile_cost_additional_lines = tmobile_cost_additional_line * num_additional_lines

    # L2
    tmobile_cost_first_two_lines = 50 # $50 per month for the first two lines
    tmobile_total_cost = tmobile_cost_first_two_lines + tmobile_cost_additional_lines

    # L3
    mmobile_cost_additional_line = 14 # $14 for each additional line
    mmobile_cost_additional_lines = mmobile_cost_additional_line * num_additional_lines

    # L4
    mmobile_cost_first_two_lines = 45 # $45 for the first two lines
    mmobile_total_cost = mmobile_cost_first_two_lines + mmobile_cost_additional_lines

    # L5
    price_difference = tmobile_total_cost - mmobile_total_cost

    # FA
    answer = price_difference
    return answer
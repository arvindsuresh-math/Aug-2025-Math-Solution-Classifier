def solve():
    """Index: 2536.
    Returns: the total money Tina earned after selling all postcards made in 6 days.
    """
    # L1
    num_days = 6 # 6 days
    postcards_per_day = 30 # she can make 30 such postcards
    total_postcards = num_days * postcards_per_day

    # L2
    money_per_postcard = 5 # For each postcard sold, Tina gets $5
    total_money = total_postcards * money_per_postcard

    # FA
    answer = total_money
    return answer
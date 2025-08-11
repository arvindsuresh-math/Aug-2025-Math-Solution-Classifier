def solve():
    """Index: 4740.
    Returns: the total number of muffins for sale.
    """
    # L1
    num_boys = 3 # 3 boys
    muffins_per_boy = 12 # each make 12 muffins
    boys_total_muffins = num_boys * muffins_per_boy

    # L2
    num_girls = 2 # 2 other girls
    muffins_per_girl = 20 # making 20 muffins each
    girls_total_muffins = num_girls * muffins_per_girl

    # L3
    total_muffins = boys_total_muffins + girls_total_muffins

    # FA
    answer = total_muffins
    return answer
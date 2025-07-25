def solve():
    """Index: 7369.
    Returns: the number of carrots Wilfred needs to eat on Thursday.
    """
    # L1
    carrots_tuesday = 4 # 4 carrots on Tuesday
    carrots_wednesday = 6 # 6 carrots on Wednesday
    carrots_tuesday_wednesday = carrots_tuesday + carrots_wednesday

    # L2
    total_carrots_target = 15 # total of 15 carrots
    carrots_thursday = total_carrots_target - carrots_tuesday_wednesday

    # FA
    answer = carrots_thursday
    return answer
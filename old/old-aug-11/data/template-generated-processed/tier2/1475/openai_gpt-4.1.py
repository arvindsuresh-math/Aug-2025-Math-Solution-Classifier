def solve():
    """Index: 1475.
    Returns: the total number of marbles Pete has after trading with his friend.
    """
    # L1
    total_marbles = 10 # Pete has a bag with 10 marbles
    blue_percent_decimal = 0.4 # 40% are blue
    blue_marbles = total_marbles * blue_percent_decimal

    # L2
    percent_total = 100 # WK
    blue_percent = 40 # 40% are blue
    red_percent = percent_total - blue_percent

    # L3
    red_percent_decimal = 0.6 # 60% of the marbles are red
    red_marbles = total_marbles * red_percent_decimal

    # L4
    red_marbles_kept = 1 # keeps 1 red marble
    red_marbles_traded = red_marbles - red_marbles_kept

    # L5
    blue_per_red = 2 # two blue marbles for every red one # WK
    blue_marbles_gained = red_marbles_traded * blue_per_red

    # L6
    # blue_marbles (original blue), red_marbles_kept (kept red), blue_marbles_gained (gained blue)
    total_after_trade = blue_marbles + red_marbles_kept + blue_marbles_gained

    # FA
    answer = total_after_trade
    return answer
def solve():
    """Index: 4182.
    Returns: the total money Darryl made from selling melons.
    """
    # L1
    initial_cantaloupes = 30 # started the day with 30 cantaloupes
    dropped_cantaloupes = 2 # dropped a couple of cantaloupes
    remaining_cantaloupes = 8 # had 8 cantaloupes and 9 honeydews left
    sold_cantaloupes = initial_cantaloupes - dropped_cantaloupes - remaining_cantaloupes

    # L2
    initial_honeydews = 27 # started the day with 27 honeydews
    rotten_honeydews = 3 # three of the honeydews turned out to be rotten
    remaining_honeydews = 9 # had 9 honeydews left
    sold_honeydews = initial_honeydews - rotten_honeydews - remaining_honeydews

    # L3
    price_cantaloupe = 2 # cantaloupes for $2 each
    revenue_cantaloupes = sold_cantaloupes * price_cantaloupe

    # L4
    price_honeydew = 3 # honeydews for $3
    revenue_honeydews = sold_honeydews * price_honeydew

    # L5
    total_money_made = revenue_cantaloupes + revenue_honeydews

    # FA
    answer = total_money_made
    return answer
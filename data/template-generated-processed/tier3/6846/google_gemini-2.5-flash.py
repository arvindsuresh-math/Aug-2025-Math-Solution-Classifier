def solve():
    """Index: 6846.
    Returns: the total amount of money each shopper will receive.
    """
    # L1
    giselle_money = 120 # Giselle has $120
    isabella_more_than_giselle = 15 # only $15 more than Giselle
    isabella_money = giselle_money + isabella_more_than_giselle

    # L2
    isabella_giselle_combined = isabella_money + giselle_money

    # L3
    isabella_more_than_sam = 45 # Isabella has $45 more than Sam
    sam_money = isabella_money - isabella_more_than_sam

    # L4
    total_money = isabella_giselle_combined + sam_money

    # L5
    num_shoppers = 3 # three shoppers
    money_per_shopper = total_money / num_shoppers

    # FA
    answer = money_per_shopper
    return answer
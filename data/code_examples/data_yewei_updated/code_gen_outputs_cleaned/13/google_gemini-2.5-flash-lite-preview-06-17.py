def solve(
    cheddar_pounds: int = 2, # He buys 2 pounds of cheddar cheese
    cheddar_price_per_pound: int = 10, # for $10
    cream_cheese_pounds: int = 1, # a pound of cream cheese
    cold_cuts_packs: int = 1 # and a pack of cold cuts
):
    """Index: 13.
    Returns: the total amount Jasper spent on the ingredients.
    """
    #: L1
    cream_cheese_price_per_pound = cheddar_price_per_pound / 2

    #: L2
    cold_cuts_price = cheddar_price_per_pound * 2

    #: L3
    total_spent = (cheddar_pounds * cheddar_price_per_pound) + (cream_cheese_pounds * cream_cheese_price_per_pound) + (cold_cuts_packs * cold_cuts_price)

    answer = total_spent # FINAL ANSWER
    return answer
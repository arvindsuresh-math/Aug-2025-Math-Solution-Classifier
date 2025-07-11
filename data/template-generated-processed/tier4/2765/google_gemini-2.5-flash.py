def solve():
    """Index: 2765.
    Returns: the number of people who ordered chocolate ice cream.
    """
    # L1
    total_customers = 220 # 220 people ordered ice cream on Saturday
    vanilla_ordered_decimal = 0.2 # 20% of those ordered vanilla ice cream
    vanilla_customers = vanilla_ordered_decimal * total_customers

    # L2
    vanilla_to_chocolate_factor = 2 # twice as many people who ordered vanilla as ordered chocolate
    chocolate_customers = vanilla_customers / vanilla_to_chocolate_factor

    # FA
    answer = chocolate_customers
    return answer
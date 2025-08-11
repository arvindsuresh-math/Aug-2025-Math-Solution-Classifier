def solve():
    """Index: 2765.
    Returns: the number of people who ordered chocolate ice cream.
    """
    # L1
    total_customers = 220 # 220 people ordered ice cream on Saturday
    vanilla_percent = 0.2 # 20% of those ordered vanilla ice cream
    vanilla_customers = vanilla_percent * total_customers

    # L2
    chocolate_customers = vanilla_customers / 2

    # FA
    answer = chocolate_customers
    return answer
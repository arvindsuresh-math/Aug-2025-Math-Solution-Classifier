def solve():
    """Index: 2809.
    Returns: the maximum dollar value of improvements Jenny can make before her property tax bill exceeds what she can afford.
    """
    # L1
    initial_value = 400000 # house is currently worth $400,000
    rail_increase_percent = 0.25 # increase by 25%
    rail_increase_amount = initial_value * rail_increase_percent

    # L2
    new_value_after_rail = rail_increase_amount + initial_value

    # L3
    max_affordable_tax = 15000 # can only afford to spend $15,000/year
    property_tax_rate = 0.02 # property tax rate is 2%
    max_house_value = max_affordable_tax / property_tax_rate

    # L4
    max_improvement_value = max_house_value - new_value_after_rail

    # FA
    answer = max_improvement_value
    return answer
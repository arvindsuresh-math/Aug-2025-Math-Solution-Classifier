def solve():
    """Index: 2809.
    Returns: the maximum value of improvements Jenny can make to her house.
    """
    # L1
    initial_house_value = 400000 # house is currently worth $400,000
    value_increase_percent_num = 25 # increase her house's value by 25%
    value_increase_percent_decimal = 0.25 # from solution text: *.25
    value_increase_amount = initial_house_value * value_increase_percent_decimal

    # L2
    new_house_value = value_increase_amount + initial_house_value

    # L3
    affordable_tax_limit = 15000 # afford to spend $15,000/year on property tax
    property_tax_rate_percent = 2 # property tax rate is 2%
    property_tax_rate_decimal = 0.02 # from solution text: /.02
    max_house_value = affordable_tax_limit / property_tax_rate_decimal

    # L4
    improvements_value = max_house_value - new_house_value

    # FA
    answer = improvements_value
    return answer
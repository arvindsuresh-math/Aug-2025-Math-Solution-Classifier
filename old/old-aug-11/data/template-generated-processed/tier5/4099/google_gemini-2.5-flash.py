def solve():
    """Index: 4099.
    Returns: the number of tons of copper Big Dig Mining Company mines daily.
    """
    # L2
    total_percentage = 100 # WK
    nickel_percentage_q = 10 # 10% of their output is nickel
    iron_percentage_q = 60 # 60% is iron
    copper_percentage = total_percentage - nickel_percentage_q - iron_percentage_q

    # L4
    tons_of_nickel_mined_daily = 720 # They mine 720 tons of nickel a day.
    percentage_used_for_total_calc = 60 # 60% is iron (used by solution in calculation for total output)
    total_ore_output = total_percentage * tons_of_nickel_mined_daily / percentage_used_for_total_calc

    # L5
    copper_tons_daily = total_ore_output * copper_percentage / total_percentage

    # FA
    answer = copper_tons_daily
    return answer
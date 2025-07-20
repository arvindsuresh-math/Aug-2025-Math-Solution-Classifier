def solve():
    """Index: 7379.
    Returns: the total profit each son can make in a year.
    """
    # L1
    total_hectares = 3 # 3 hectares of land
    sq_m_per_hectare = 10000 # 1 hectare is equal to 10000 m^2
    total_land_sq_m = total_hectares * sq_m_per_hectare

    # L2
    num_sons = 8 # 8 sons
    land_per_son_sq_m = total_land_sq_m / num_sons

    # L3
    profit_area_unit = 750 # every 750m^2 of this land
    num_profit_portions_per_son = land_per_son_sq_m / profit_area_unit

    # L4
    profit_per_portion = 500 # profit of $500
    profit_per_son_per_3_months = num_profit_portions_per_son * profit_per_portion

    # L5
    months_per_year = 12 # one year there are 12 months
    profit_period_months = 3 # every 3 months
    num_profit_periods_per_year = months_per_year / profit_period_months

    # L6
    total_profit_per_son_per_year = profit_per_son_per_3_months * num_profit_periods_per_year

    # FA
    answer = total_profit_per_son_per_year
    return answer
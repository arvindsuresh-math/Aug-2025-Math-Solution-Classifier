def solve():
    """Index: 7252.
    Returns: the total amount Jim has spent on gas.
    """
    # L1
    nc_gallons = 10 # 10 gallons of gas
    nc_price_per_gallon = 2.00 # $2.00/gallon
    nc_total_cost = nc_gallons * nc_price_per_gallon

    # L2
    virginia_price_increase = 1.00 # $1.00 more per gallon
    va_price_per_gallon = nc_price_per_gallon + virginia_price_increase

    # L3
    va_gallons = 10 # another 10 gallons of gas
    va_total_cost = va_gallons * va_price_per_gallon

    # L4
    total_spent = nc_total_cost + va_total_cost

    # FA
    answer = total_spent
    return answer
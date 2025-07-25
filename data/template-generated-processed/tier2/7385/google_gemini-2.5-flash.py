def solve():
    """Index: 7385.
    Returns: the amount Bob sells the silver for.
    """
    # L1
    side_length = 3 # 3 inches on each side
    volume_cubic_inches = side_length * side_length * side_length

    # L2
    weight_per_cubic_inch = 6 # A cubic inch of silver weighs 6 ounces
    total_weight_ounces = volume_cubic_inches * weight_per_cubic_inch

    # L3
    price_per_ounce = 25 # Each ounce of silver sells for $25
    silver_value = total_weight_ounces * price_per_ounce

    # L4
    sale_percentage_decimal = 1.1 # 110% of its silver value
    final_sale_price = silver_value * sale_percentage_decimal

    # FA
    answer = final_sale_price
    return answer
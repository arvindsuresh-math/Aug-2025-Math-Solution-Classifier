def solve():
    """Index: 1839.
    Returns: the combined weight of the donkey and elephant in pounds.
    """
    # L1
    elephant_weight_tons = 3 # The elephant weighs 3 tons
    pounds_per_ton = 2000 # a ton is 2000 pounds
    elephant_weight_pounds = elephant_weight_tons * pounds_per_ton

    # L2
    less_percent_decimal = 0.9 # 90% less
    donkey_weight_less_amount = elephant_weight_pounds * less_percent_decimal

    # L3
    donkey_weight_pounds = elephant_weight_pounds - donkey_weight_less_amount

    # L4
    combined_weight_pounds = donkey_weight_pounds + elephant_weight_pounds

    # FA
    answer = combined_weight_pounds
    return answer